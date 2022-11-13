import os
import pytest
from pathlib import Path
import comp630 
import boto3
from moto import mock_s3

"""os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'"""


# test bucket specific to class and person
TEST_BUCKET = "comp630-m1-f21-lab1116"
TEST_FILE = "lab1116.moto"

@mock_s3
def test_upload():
    moto_credentials_file_path = Path(__file__).parent.absolute() / 'dummy_aws_credentials'
    """os.environ['AWS_SHARED_CREDENTIALS_FILE'] = str(moto_credentials_file_path)
    os.environ['AWS_ACCESS_KEY_ID'] = 'test'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'"""
    # make scope global
    global TEST_BUCKET
    global TEST_FILE
    # With the moto library imported, the boto3 s3 is fake
    conn = boto3.client("s3", region_name="us-east-1")
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    conn.create_bucket(Bucket=TEST_BUCKET)
    with open(TEST_FILE, "rb") as f:
        object_name = os.path.basename(f.name)
        comp630.to_the_cloud(f.name, TEST_BUCKET, TEST_FILE)

    assert True
