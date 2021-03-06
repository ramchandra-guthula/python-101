import boto3
from pprint import pprint

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='eu-west-1')
"""
# describe = cloudwatch.describe_alarms()
# pprint(describe)
"""

# Create alarm with actions enabled

cloudwatch.put_metric_alarm(
    AlarmName='ec2_Recover',
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    EvaluationPeriods=1,
    MetricName='StatusCheckFailed_System',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Sum',
    Threshold=1.0,
    ActionsEnabled=True,
    AlarmActions=[
      'arn:aws:swf:eu-west-1:{CUSTOMER_ACCOUNT}:action/actions/AWS_EC2.InstanceId.Recover/1.0'
    ],
    AlarmDescription='Recover the instance when systemchecks fails',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'i-0238d9522ac8abdfc'
        },
    ],
    Unit='Seconds'
)
