import boto3
ec2=boto3.resource('ec2')
vpc = ec2.create_vpc(
    CidrBlock='172.16.0.0/16',
    # AmazonProvidedIpv6CidrBlock=False,
    # Ipv6Pool='string',
    # Ipv6CidrBlock='string',
    DryRun=False,
    InstanceTenancy='default',
    # Ipv6CidrBlockNetworkBorderGroup='string',
    TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'name',
                    'Value': 'shakeer'
                },
            ]
        },
    ]
)
vpc.create_tags(Tags=[{"Key": "Name", "Value": "Shakeervpc"}])
print (vpc)
ec2Client = boto3.client('ec2')
ec2Client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsSupport = { 'Value': True } )
ec2Client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsHostnames = { 'Value': True } )
###internet gateway
internetgateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)
print (internetgateway)
# create a route table and a public route
routetable = vpc.create_route_table()
route = routetable.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internetgateway.id)
print (routetable)
# create subnet and associate it with route table
subnet = ec2.create_subnet(CidrBlock='172.16.1.0/24', VpcId=vpc.id)
routetable.associate_with_subnet(SubnetId=subnet.id)
print (subnet)
# Create a security group and allow SSH inbound rule through the VPC
securitygroup = ec2.create_security_group(GroupName='SSH-ONLY', Description='only allow SSH traffic', VpcId=vpc.id)
securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)
print (securitygroup)
# create a file to store the key locally
outfile = open('ec2new2-keypair.pem', 'w')

# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2new2-keypair')

# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)

# Create a linux instance in the subnet
instances = ec2.create_instances(
 ImageId='ami-02f26adf094f51167',
 InstanceType='t2.micro',
 MaxCount=1,
 MinCount=1,
 NetworkInterfaces=[{
 'SubnetId': subnet.id,
 'DeviceIndex': 0,
 'AssociatePublicIpAddress': True,
 'Groups': [securitygroup.group_id]
 }],
 KeyName='ec2new2-keypair')

print (instances)
