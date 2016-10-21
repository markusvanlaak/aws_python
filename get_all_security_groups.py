import boto3

ec2 = boto3.resource('ec2')

security_group = ec2.SecurityGroup('sg-4ae39a22')

print security_group.group_name()
