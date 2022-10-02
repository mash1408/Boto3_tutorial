import boto3
from boto3 import Session
from botocore import exceptions
import io
import paramiko


key = paramiko.RSAKey.from_private_key_file('./AWS/Passkey.pem')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

session = Session()
credentials = session.get_credentials()
# Credentials are refreshable, so accessing your access key / secret key
# separately can lead to a race condition. Use this to get an actual matched
# set.
current_credentials = credentials.get_frozen_credentials()
commands=["sudo wget https://bucket4600.s3.ap-northeast-1.amazonaws.com/index.html"]

AWS_REGION='ap-northeast-1'
location = {'LocationConstraint': AWS_REGION}
s3_client = boto3.client('s3',aws_access_key_id=current_credentials.access_key,
    aws_secret_access_key=current_credentials.secret_key,region_name=AWS_REGION)
ec2_client=boto3.client('ec2',aws_access_key_id=current_credentials.access_key,
    aws_secret_access_key=current_credentials.secret_key,region_name=AWS_REGION)
ssm_client = boto3.client('ssm',aws_access_key_id=current_credentials.access_key,
    aws_secret_access_key=current_credentials.secret_key,region_name=AWS_REGION)

def create_bucket(bucket_name):
    s3_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)

def upload_file_to_bucket(bucket_name,obj_url):
    s3_client.upload_file(obj_url,bucket_name,'error.html')

def get_object_from_bucket(bucket_name):
    res=s3_client.get_object(
        Bucket=bucket_name,
        Key='error.html'
    )
    return res
def download_file_from_bucket(bucket_name,key_name):
    data=io.BytesIO()
    s3_client.download_fileobj(bucket_name, key_name, data)
    return data

def launch_instance():
    try:
        INSTANCE_TYPE = 't2.micro'  #These will be environment variables that we must specify in lambda
        KEY_NAME = 'password'
        AMI_ID='ami-078296f82eb463377'
        SUBNET_ID='subnet-0228a5957b880ad99'
        instance = ec2_client.run_instances(
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            ImageId=AMI_ID,
            SubnetId=SUBNET_ID,
            MaxCount=1,
            MinCount=1,
            DryRun=True,
            TagSpecifications=[{    #This creates a tag for our resource
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'TestCase'}]
            }]
        )
        print("New instance created:", instance[0].id)
    except Exception as e:
        print("An error occured "+str(e))
    


def execute_command_on_instances(client, commands, instance_ids,bucket_name):
    '''To execute a command on an instance using the SSM client setup on the target machine'''
    commands= " ".join(["sudo wget https://",bucket_name,".s3.ap-northeast-1.amazonaws.com/index.html"])
    resp = client.send_command(
        DocumentName="AWS-RunShellScript", # One of AWS' preconfigured documents
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
    )
    return resp

# SSH Method
def ssh_and_run_commands(instance_ip):
    '''This method will wrap ssh commands and execute on target machine'''
    print(instance_ip)
    client.connect(hostname=instance_ip, username="ubuntu", pkey=key)

        # Execute a command(cmd) after connecting/ssh to an instance
    stdin, stdout, stderr = client.exec_command('aws s3 cp s3://bucket4600/index.html ./index.html')
    print(stdout.read())
        # close the client connection once the job is done
    client.close()

def get_public_ip_ec2(instance_id):
    '''Helper function for SSH'''
    reservations = ec2_client.describe_instances(InstanceIds=instance_id).get("Reservations")
    p_ips=[]
    for reservation in reservations:
        for instance in reservation['Instances']:
            p_ips.append(instance['PublicIpAddress'])
    return p_ips

    

bucket_name= input('Enter Bucket Name')
file_url=input('Enter the location of the file')
res=download_file_from_bucket(bucket_name,file_url)
upload_file_to_bucket(bucket_name,file_url)
InstanceIds=[str(x) for x in input('Provide instanceID').split(' ')]
res=execute_command_on_instances(ssm_client,commands,InstanceIds,bucket_name)
# public_ips=get_public_ip_ec2(InstanceIds)
# ssh_and_run_commands(public_ips[0])