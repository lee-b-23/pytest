import os
import pytest
import comp630 
import boto3
from moto import mock_s3

# test bucket specific to class and person
TEST_BUCKET = "comp630-m1-f21-lab1116"
TEST_FILE = "lab1116.moto"

@mock_s3
def test_upload():
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
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
