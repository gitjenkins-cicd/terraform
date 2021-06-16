import boto3
# creating key-pairs for accessing vm
ec2=boto3.resource('ec2')
outfile=open('ec2-keypair.pem','w')
key_pair=ec2.create_key_pair(keyname='ec2-keypair')
key_pair_out=str(key_pair.key_material)
print(key_pair_out)
outfile.write(key_pair_out)
# Creating VM

ec2=boto3.resource('ec2')
instances=ec2.create_instances(
ImageId='ami-00b6a8a2bd28daf19',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
)

import google.cloud