import boto3
from datetime import datetime, timezone

def rerun_failed_executions(state_machine_arn, start_date):
    # Create a Step Functions client
    client = boto3.client('stepfunctions')

    # Convert the start_date string to a datetime object with timezone information
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)

    # List all executions of the specified state machine
    response = client.list_executions(stateMachineArn=state_machine_arn)

    # Filter and rerun failed executions since the start date
    for execution in response['executions']:
        execution_arn = execution['executionArn']
        execution_start_date = execution['startDate'].replace(tzinfo=timezone.utc)

        # Check if the execution failed and started after the specified start date
        if execution['status'] == 'FAILED' and execution_start_date > start_datetime:
            # Get the input of the failed execution
            execution_details = client.describe_execution(executionArn=execution_arn)
            execution_input = execution_details['input']

            # Skip if the execution_input is an empty dictionary
            if execution_input == '{}':
                print(f"Skipping execution: {execution_arn} as input is empty")
                continue

            # Generate a unique name for the new execution using the current timestamp
            name = f"RetryExecution_{datetime.now().strftime('%Y%m%d%H%M%S')}"

            # Initiate a new execution with the input of the failed execution
            response = client.start_execution(
                stateMachineArn=state_machine_arn,
                name=name,
                input=execution_input
            )

            # Print the details of the newly started execution
            print(f"Rerunning execution: {execution_arn}")
            print(f"New execution ARN: {response['executionArn']}")

# Specify your Step Functions state machine ARN
state_machine_arn = 'arn:aws:states:us-west-2:123456789012:stateMachine:MyStateMachine'

# Specify the start date in the format 'YYYY-MM-DD HH:MM:SS'
start_date = '2023-05-01 00:00:00'

# Call the function to rerun failed executions since the specified start date
rerun_failed_executions(state_machine_arn, start_date)
