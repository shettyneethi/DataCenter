#!/usr/bin/env python

import argparse
import os
import time
from pprint import pprint

import googleapiclient.discovery
import google.auth

ZONE = 'us-west1-b'
INSTANCE_NAME = 'lab5'
DISK = 'lab5' 
SNAPSHOT_NAME ="base-snapshot-lab5"

credentials, project = google.auth.default()
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

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

def createInstanceFromSnapshot(i):
	disk_body = {
				  "name": "replica"+str(i),
				  "sourceSnapshot": "projects/%s/global/snapshots/%s" %(project,SNAPSHOT_NAME)
				}
	response = service.disks().insert(project=project, zone=ZONE, body=disk_body).execute()
	wait_for_operation(service, project, ZONE, response['name'])

	startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
	config = {
		  "name": "instance"+str(i),
		  "machineType": "zones/%s/machineTypes/f1-micro" % ZONE,
		   "tags": {
			    "items": ["allow-5000"]
			},
		  "networkInterfaces": [{
	            'network': 'global/networks/default',
	            'accessConfigs': [
	                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
	            ]
	        }],
		  "disks": [{
		     "source": "zones/%s/disks/replica%s" % (ZONE,i),
		     "boot": True
		   }],
		   'metadata': {
	            'items': [{
	                # Startup script is automatically executed by the
	                # instance upon startup.
	                'key': 'startup-script',
	                'value': startup_script
	            }]
        	}
		}
	start_time = time.time()
	operation = service.instances().insert(project=project,zone=ZONE,body=config).execute()
	wait_for_operation(service, project, ZONE, operation['name'])
	recordTime.write(str(i) + "Instance creation time : " + str(time.time() - start_time) + "\n")
	return

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None


snapshot_body = {
  "name": SNAPSHOT_NAME
}

operation = service.disks().createSnapshot(project=project, zone=ZONE, disk=DISK, body=snapshot_body).execute()
wait_for_operation(service, project, ZONE, operation['name'])

with open("TIMING.md",'w') as recordTime:
	for i in range(3):
		createInstanceFromSnapshot(i+1)
		
print("Your running instances are:")
for instance in list_instances(service, project, ZONE):
    print(instance['name'])