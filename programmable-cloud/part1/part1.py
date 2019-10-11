import argparse
import os
import time
from pprint import pprint

import googleapiclient.discovery
import google.auth

credentials, project = google.auth.default()
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

BUCKET = 'sneethi'
ZONE = 'us-west1-b'
INSTANCE_NAME = 'lab5'

# [START create_instance]
def create_instance(compute, project, zone, name, bucket):
    image_response = compute.images().getFromFamily(
        project='ubuntu-os-cloud', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = "zones/%s/machineTypes/f1-micro" % ZONE
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    image_url = "http://storage.googleapis.com/gce-demo-input/photo.jpg"
    image_caption = "Ready for dessert?"

    config = {
        'name': name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }]
        }
    }

    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
# [END create_instance]

# [START wait_for_operation]
def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)
# [END wait_for_operation]

# [START list_instances]
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None
# [END list_instances]

total_time = 0
print('Creating instance.')
start_time = time.time()
operation = create_instance(service, project, ZONE, INSTANCE_NAME, BUCKET)
wait_for_operation(service, project, ZONE, operation['name'])
total_time = time.time() - start_time

print("Your running instances are:")
for instance in list_instances(service, project, ZONE):
    print(instance['name'])

firewall_body = {
					"name": "allow-5000",
					"sourceRanges": ["0.0.0.0/0"],
					"targetTags": ["allow-5000"],
					"allowed": [
								    {
								      "IPProtocol": "TCP",
								      "ports": ["5000"]
								    }
								]
				}

request = service.firewalls().list(project=project)

isFirewallCreated = False
while request is not None:
    response = request.execute()
    print("EXISTING FIREWALLS : ")
    for firewall in response['items']:
    	print(str(firewall['name']))
    	if(str(firewall['name']) == "allow-5000"):
        	isFirewallCreated = True
    request = service.firewalls().list_next(previous_request=request, previous_response=response)

if not isFirewallCreated:
	request = service.firewalls().insert(project=project, body=firewall_body)
	response = request.execute()
	pprint(response)


start_time = time.time()
instance_details = service.instances().get(project=project, zone=ZONE, instance=INSTANCE_NAME).execute()
fingerprint = instance_details['tags']['fingerprint']
tags_body = {
    "items" : [ "allow-5000" ],
    "fingerprint" : fingerprint
}
request = service.instances().setTags(project=project, zone=ZONE, instance=INSTANCE_NAME, body=tags_body)
response = request.execute()
wait_for_operation(service, project, ZONE, response['name'])
total_time += time.time() - start_time

with open("TIMING.md",'w') as recordTime:
    recordTime.write("Original VM took: %s" % str(total_time))
print("Please visit: http://{}:5000".format(instance_details["networkInterfaces"][0]["accessConfigs"][0]["natIP"]))