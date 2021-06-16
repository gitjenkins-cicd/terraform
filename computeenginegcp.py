import boto3
ec2=boto3.resource('ec2')
instance = ec2.create_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': 'Shakeer',
            'VirtualName': 'Shakeer',
            'Ebs': {
                'DeleteOnTermination': True,
                'Iops': 50,
                'SnapshotId': 'snap-0f275b20d01751454',
                'VolumeSize': 123,
                'VolumeType': 'gp2',
                # 'KmsKeyId': 'string',
                'Throughput': 123,
                # 'OutpostArn': 'string',
                'Encrypted': True
            },
            'NoDevice': 'Nodevice'
        },
    ],
    ImageId='ami-02f26adf094f5116',
    InstanceType='t2.micro',
    Ipv6AddressCount=123,
    Ipv6Addresses=[
        {
            'Ipv6Address': 'string'
        },
    ],
    KernelId='string',
    KeyName='string',
    MaxCount=5,
    MinCount=1,
    Monitoring={
        'Enabled': True|False
    },
    Placement={
        'AvailabilityZone': 'string',
        'Affinity': 'string',
        'GroupName': 'string',
        'PartitionNumber': 123,
        'HostId': 'string',
        'Tenancy': 'default'|'dedicated'|'host',
        'SpreadDomain': 'string',
        'HostResourceGroupArn': 'string'
    },
    RamdiskId='string',
    SecurityGroupIds=[
        'string',
    ],
    SecurityGroups=[
        'string',
    ],
    SubnetId='string',
    UserData='string',
    AdditionalInfo='string',
    ClientToken='string',
    DisableApiTermination=True|False,
    DryRun=True|False,
    EbsOptimized=True|False,
    IamInstanceProfile={
        'Arn': 'string',
        'Name': 'string'
    },
    InstanceInitiatedShutdownBehavior='stop'|'terminate',
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True|False,
            'DeleteOnTermination': True|False,
            'Description': 'string',
            'DeviceIndex': 123,
            'Groups': [
                'string',
            ],
            'Ipv6AddressCount': 123,
            'Ipv6Addresses': [
                {
                    'Ipv6Address': 'string'
                },
            ],
            'NetworkInterfaceId': 'string',
            'PrivateIpAddress': 'string',
            'PrivateIpAddresses': [
                {
                    'Primary': True|False,
                    'PrivateIpAddress': 'string'
                },
            ],
            'SecondaryPrivateIpAddressCount': 123,
            'SubnetId': 'string',
            'AssociateCarrierIpAddress': True|False,
            'InterfaceType': 'string',
            'NetworkCardIndex': 123
        },
    ],
    PrivateIpAddress='string',
    ElasticGpuSpecification=[
        {
            'Type': 'string'
        },
    ],
    ElasticInferenceAccelerators=[
        {
            'Type': 'string',
            'Count': 123
        },
    ],
    TagSpecifications=[
        {
            'ResourceType': 'client-vpn-endpoint'|'customer-gateway'|'dedicated-host'|'dhcp-options'|'egress-only-internet-gateway'|'elastic-ip'|'elastic-gpu'|'export-image-task'|'export-instance-task'|'fleet'|'fpga-image'|'host-reservation'|'image'|'import-image-task'|'import-snapshot-task'|'instance'|'internet-gateway'|'key-pair'|'launch-template'|'local-gateway-route-table-vpc-association'|'natgateway'|'network-acl'|'network-interface'|'network-insights-analysis'|'network-insights-path'|'placement-group'|'reserved-instances'|'route-table'|'security-group'|'snapshot'|'spot-fleet-request'|'spot-instances-request'|'subnet'|'traffic-mirror-filter'|'traffic-mirror-session'|'traffic-mirror-target'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-connect-peer'|'transit-gateway-multicast-domain'|'transit-gateway-route-table'|'volume'|'vpc'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway'|'vpc-flow-log',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    LaunchTemplate={
        'LaunchTemplateId': 'string',
        'LaunchTemplateName': 'string',
        'Version': 'string'
    },
    InstanceMarketOptions={
        'MarketType': 'spot',
        'SpotOptions': {
            'MaxPrice': 'string',
            'SpotInstanceType': 'one-time'|'persistent',
            'BlockDurationMinutes': 123,
            'ValidUntil': datetime(2015, 1, 1),
            'InstanceInterruptionBehavior': 'hibernate'|'stop'|'terminate'
        }
    },
    CreditSpecification={
        'CpuCredits': 'string'
    },
    CpuOptions={
        'CoreCount': 123,
        'ThreadsPerCore': 123
    },
    CapacityReservationSpecification={
        'CapacityReservationPreference': 'open'|'none',
        'CapacityReservationTarget': {
            'CapacityReservationId': 'string',
            'CapacityReservationResourceGroupArn': 'string'
        }
    },
    HibernationOptions={
        'Configured': True|False
    },
    LicenseSpecifications=[
        {
            'LicenseConfigurationArn': 'string'
        },
    ],
    MetadataOptions={
        'HttpTokens': 'optional'|'required',
        'HttpPutResponseHopLimit': 123,
        'HttpEndpoint': 'disabled'|'enabled'
    },
    EnclaveOptions={
        'Enabled': True|False
    }
)

)