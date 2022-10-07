
from operator import contains
from urllib import response
import boto3
#create an object for s3 service
s3_client = boto3.client('s3',region_name='ap-south-1')
#create bucket

#response = boto3.client.create_bucket(
    
 #   Bucket='reddy-s3-aws',
  #  CreateBucketConfiguration={
   #     'LocationConstriant': 'ap-sount-1'
    #},
    
#)
#print('response')

#upload a file to s3 bucket
'''
response = s3_client.put_object(
    Body=open("s3.py",'r').read(),
    Bucket = 'reddy-s3-aws',
    key = 's3.py'
)
print('response')

#download a files  to local system
response = s3_client.get.object(
    Bucket = 'reddy-s3-aws',33
    key='s3.py'
    
)
data= response.get('Body').read().decode()
file = open("s3.py","w")
file.writelines(data)
file.close() 
'''
#list of buckets
'''
response = s3_client.list_buckets()
buckets = response.get("Buckets")

print(f"Total buckets : {len(buckets)}")
print(buckets)
'''
#list of objects
'''
response=s3_client.list_objects(
    Bucket = 'reddy-s3-aws'
)
objects = response.get("Contents")

print(f"Total objects: {len(objects)}")
print(objects)
'''
#delete object
'''
response=s3_client.list_object(
    Bucket = 'reddy-s3-aws',
    key='s3.py'
)
print(response)
'''
#delete bucket
response=s3_client.delete_bucket(
    Bucket = 'reddy-s3-aws'
)
print(response)