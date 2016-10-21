import boto3

ec2 = boto3.resource('ec2')

for i in ec2.instances.all(): print (i)

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)

for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]): print (i)

    
#add tags

mytags = [{
    "Key" : "Name",
            "Value" : "GIG 3"
    }]

for i in ec2.security_groups.all(): id.append(i.id)
    for id_sg in id:
        ec2.create_tags(Resources = [id_sg],Tags= mytags)
