#  [CloudFormation](https://github.com/rahulmlokurte/script-hub/blob/main/AWS/cloudformation)

## [drift_detection](https://github.com/rahulmlokurte/script-hub/blob/main/AWS/cloudformation/drift_detection.py)

This utility Python script allows you to detect whether a stack's actual configuration differs, or has drifted, from its expected configuration. This will happen, when user manually changes the configuration.

### Prerequisites

:bulb: Set the below environment variables for your AWS account
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

### Steps to run
 
1. Specify the stack name prefixes to the variable `stack_name_prefixes` in `drift_detection.py`. It supports an array of stack names.