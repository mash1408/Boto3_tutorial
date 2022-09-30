import boto3
from boto3 import Session
from botocore import exceptions
import io

session = Session()
credentials = session.get_credentials()
# Credentials are refreshable, so accessing your access key / secret key
# separately can lead to a race condition. Use this to get an actual matched
# set.
current_credentials = credentials.get_frozen_credentials()
commands=["mkdir Test"]

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
        print("An errorrrrrr occured     "+str(e))
    


def execute_command_on_instances(client, commands, instance_ids):
    """Runs commands on remote linux instances
    :param client: a boto/boto3 ssm client
    :param commands: a list of strings, each one a command to execute on the instances
    :param instance_ids: a list of instance_id strings, of the instances on which to execute the command
    :return: the response from the send_command function (check the boto3 docs for ssm client.send_command() )
    """

    resp = client.send_command(
        DocumentName="AWS-RunShellScript", # One of AWS' preconfigured documents
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
    )
    return resp
def test(bucket_name,file_url):
    upload_file_to_bucket(bucket_name,file_url)
    # launch_instance()

# bucket_name= input('Enter Bucket Name')
# file_url=input('Enter the location of the file')
# test(bucket_name,file_url)
# res=download_file_from_bucket(bucket_name,file_url)
InstanceIds=[x for x in input('Provide instanceID').split(' ')]
print(InstanceIds)
execute_command_on_instances(ssm_client,commands,InstanceIds)
# print(type(res))

