#!/usr/bin/env python

import argparse
import os
import time
from pprint import pprint

import googleapiclient.discovery
import google.auth
import google.oauth2.service_account as service_account

#
# Use Google Service Account - See https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.service_account.html#module-google.oauth2.service_account
#

BUCKET = 'sneethi'
ZONE = 'us-west1-b'
INSTANCE_NAME = 'part3vm1'

credentials = service_account.Credentials.from_service_account_file(filename='service-credentials.json')
project = os.getenv('datacenterlab2') or 'datacenterlab2'
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

# [START create_instance]
def create_instance(compute, project, zone, name, bucket):
    image_response = compute.images().getFromFamily(
        project='ubuntu-os-cloud', family='ubuntu-1804-lts').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = "zones/%s/machineTypes/f1-micro" % ZONE

    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script-vm1.sh'), 'r').read()

    with open( os.path.join(os.path.dirname(__file__), 'startup-script-vm2.sh')) as f:
    	startup_script_vm2 = "\n".join(f.readlines())
    	
    with open( os.path.join(os.path.dirname(__file__), 'part3B.py')) as f:
    	python_script_3B = "\n".join(f.readlines())

    with open(os.path.join(os.path.dirname(__file__), 'service-credentials.json')) as f:
    	service_account_json = "\n".join(f.readlines())

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
            },
            {
                'key': 'startupscript',
                'value': startup_script_vm2
            },
            {
                'key': 'pythonscript',
                'value': python_script_3B
            },
            {
                'key': 'serviceaccountjson',
                'value': service_account_json
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

operation = create_instance(service, project, ZONE, INSTANCE_NAME, BUCKET)
wait_for_operation(service, project, ZONE, operation['name'])