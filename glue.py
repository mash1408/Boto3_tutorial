import boto3
from boto3 import Session
session = Session()
credentials = session.get_credentials()
# Credentials are refreshable, so accessing your access key / secret key
# separately can lead to a race condition. Use this to get an actual matched
# set.
current_credentials = credentials.get_frozen_credentials()
AWS_REGION='ap-northeast-1'
location = {'LocationConstraint': AWS_REGION}
client = boto3.client('kms',aws_access_key_id=current_credentials.access_key,
    aws_secret_access_key=current_credentials.secret_key,region_name=AWS_REGION)

glueClient = boto3.client('glue')
def create_database():
    response = glueClient.create_database(
        DatabaseInput={
            'Name': 'boto3db'
        }
    )        
def create_table():
    response = glueClient.create_table(
        DatabaseName='boto3db',
        TableInput={
            'Name': 'flights_data_manual',
        'StorageDescriptor': {
        'Columns': [{
            'Name': 'year',
            'Type': 'bigint'
        }, {
            'Name': 'quarter',
            'Type': 'bigint'
        }],
        'Location': 's3://crawler-public-us-west-2/flight/2016/csv',
        'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
        'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
        'Compressed': False,
        'NumberOfBuckets': -1,
        'SerdeInfo': {
            'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
            'Parameters': {
            'field.delim': ',',
            'serialization.format': ','
            }
        },
        },
        'PartitionKeys': [{
        'Name': 'mon',
        'Type': 'string'
        }],
        'TableType': 'EXTERNAL_TABLE',
        'Parameters': {
        'EXTERNAL': 'TRUE',
        'classification': 'csv',
        'columnsOrdered': 'true',
        'compressionType': 'none',
        'delimiter': ',',
        'skip.header.line.count': '1',
        'typeOfData': 'file'
        }
        }
    )                        
create_table()                                                                                   
                                        