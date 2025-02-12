import boto3

# Create session with credentials
session = boto3.Session(
    aws_access_key_id='<abc>',
    aws_secret_access_key='<def>
)

# Create S3 resource
s3 = session.resource('s3')

# List all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
