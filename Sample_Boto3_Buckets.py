from distutils.command import upload
import boto3
from boto3 import Session
from botocore import exceptions

session = Session()
credentials = session.get_credentials()
# Credentials are refreshable, so accessing your access key / secret key
# separately can lead to a race condition. Use this to get an actual matched
# set.
current_credentials = credentials.get_frozen_credentials()

AWS_REGION='ap-northeast-1'
location = {'LocationConstraint': AWS_REGION}
client = boto3.client('s3',aws_access_key_id=current_credentials.access_key,
    aws_secret_access_key=current_credentials.secret_key,region_name=AWS_REGION)
def create_bucket():
    client.create_bucket(Bucket='samplebucketnsdfcscbjdssbh',CreateBucketConfiguration=location)

def upload_file_to_bucket():
    client.upload_file('./index.html','samplebucketnsdfbjdssbh','index.html')

def delete_bucket(bucket_name):
    try:
        client.delete_bucket(Bucket=bucket_name)
    except exceptions.ClientError as delete_ex:
        print(delete_ex.response['Error']['Message'])

def list_buckets():
    try:
        res=client.list_buckets()
        print(res)
    except exceptions.ClientError as list_ex:
        print(list_ex.response['Error']['Message'])

def check_if_bucket_is_empty(bucket_name):
    count=client.list_objects_v2(Bucket=bucket_name)['KeyCount']
    print(count)
    return  False if count else True 

def clear_objects(bucket_name):
    bucket=boto3.resource('s3').Bucket(bucket_name)
    bucket.object_versions.delete()

def get_payer_details(bucket_name):
    s3 = boto3.resource('s3')
    bucket_request_payment = s3.BucketRequestPayment(bucket_name)
    print(bucket_request_payment.payer)
    return bucket_request_payment

def get_bucket_website_config(bucket_name):
    return client.get_bucket_website(Bucket=bucket_name)
def set_website_config(bucket_name):
    website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
    }
    client.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration=website_configuration)

upload_file_to_bucket()