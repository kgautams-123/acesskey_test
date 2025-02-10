import boto3

# Create session with credentials
session = boto3.Session(
    aws_access_key_id='AKIAY3O4SOO7RDKGBHBU',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# Create S3 resource
s3 = session.resource('s3')

# List all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
