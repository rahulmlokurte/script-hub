#  [Step Functions](https://github.com/rahulmlokurte/script-hub/tree/main/AWS/step-function)

## [retry_failed_step_function](https://github.com/rahulmlokurte/script-hub/blob/main/AWS/step-function/retry_failed_step_function.py)

This utility Python script allows you to rerun failed AWS Step Function executions. It helps you streamline your workflow and minimize manual intervention in handling failed executions.

### Prerequisites

:bulb: Set the below environment variables for your AWS account
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

### Steps to run
 
1. Specify your Step Functions state machine ARN to the variable `state_machine_arn` in `retry_failed_step_function.py`
2. Specify the start date in the format `YYYY-MM-DD HH:MM:SS` to the variable `start_date` in `retry_failed_step_function.py`