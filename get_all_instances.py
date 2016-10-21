import boto3

ec2 = boto3.resource('ec2')

#Create instances
ec2.create_instances(
    DryRun=False, 
    ImageId='ami-0044b96f' , 
    MinCount=1, MaxCount=2, 
    KeyName='gig3vpc', 
    InstanceType='t2.micro', 
    SubnetId='subnet-2eda2954', 
    SecurityGroupIds=['sg-4ae39a22',]
)


for i in ec2.instances.all(): print (i)

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)

for i in ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]): 
    print (i)
    
for instance in ec2.instances.all(): 
    print (instance.id, instance.state)
    instance.start(instance.id)

    
#add tags

mytags = [{
    "Key" : "Name",
            "Value" : "GIG 3"
    }]

for i in ec2.security_groups.all(): id.append(i.id)
    for id_sg in id:
        ec2.create_tags(Resources = [id_sg],Tags= mytags)
        
#Create an instance
ec2.create_instances(
    DryRun=True,
    ImageId='ami-0044b96f' , 
    MinCount=1, 
    MaxCount=5, 
    KeyName='gig3vpc', 
    InstanceType='t2.micro', 
    SubnetId='subnet-2eda2954'
)

