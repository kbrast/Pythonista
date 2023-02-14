import boto3
from pprint import pprint
import pathlib
import os

def upload_file_using_client():
    """
    Uploads file to S3 bucket using S3 client object
    :return: None
    """
    s3 = boto3.client("s3")
    bucket_name = "binary-guy-frompython-1"
    object_name = "sample1.txt"
    file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "sample_file.txt")

    response = s3.upload_file(file_name, bucket_name, object_name)
    pprint(response)  # prints None
