import boto3

ec2 = boto3.resource('ec2')

security_groups = ec2.get_all_security_groups()
print security_groups
