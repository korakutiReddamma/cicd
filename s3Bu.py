import boto3
aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("aws_s3_reddy_tech")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-2'
    },
   
)
print(response)