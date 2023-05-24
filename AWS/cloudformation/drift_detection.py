import json

import boto3
import time

# Create a Boto3 CloudFormation client
client = boto3.client('cloudformation')

# Specify the stack name prefixes and region
stack_name_prefixes = ['stackname1', 'stackname2']

# Iterate over the stack name prefixes
for prefix in stack_name_prefixes:
    # List stacks with the specified prefix
    response = client.list_stacks(StackStatusFilter=['CREATE_COMPLETE', 'UPDATE_COMPLETE'])
    stacks = response['StackSummaries']

    # Iterate over the stacks and detect stack drift, then describe stack resource drifts
    for stack in stacks:
        stack_name = stack['StackName']
        if stack_name.startswith(prefix):
            # Detect stack drift
            response = client.detect_stack_drift(StackName=stack_name)
            stack_drift_detection_id = response['StackDriftDetectionId']

            # Wait for stack drift detection to complete
            while True:
                response = client.describe_stack_drift_detection_status(StackDriftDetectionId=stack_drift_detection_id)
                status = response['DetectionStatus']
                if status in ['DETECTION_COMPLETE', 'DETECTION_FAILED']:
                    break
                time.sleep(5)

            # Check if drift detection was successful
            if status == 'DETECTION_FAILED':
                print(f"Stack drift detection failed for stack: {stack_name}")
                continue

            # Describe stack resource drifts
            response = client.describe_stack_resource_drifts(StackName=stack_name)
            stack_resource_drifts = response['StackResourceDrifts']

            # Process and display the stack resource drifts
            if stack_resource_drifts:
                print(f"Stack Name: {stack_name}")
                for drift in stack_resource_drifts:
                    if drift['PropertyDifferences']:
                        print("PhysicalResourceId:", drift['PhysicalResourceId'])
                        print("ResourceType:", drift['ResourceType'])
                        print("PropertyDifferences:", json.dumps(drift['PropertyDifferences'], indent=4))
                        print()
