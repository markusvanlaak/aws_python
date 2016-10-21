import boto3

ec2 = boto3.resource('ec2')

for i in ec2.instances.all(): print (i)

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)

for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]): print (i)
