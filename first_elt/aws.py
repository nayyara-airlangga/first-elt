import boto3

from configparser import ConfigParser


def config_aws():
    global account_id, access_key, secret_key, s3_bucket_name

    parser = ConfigParser()
    parser.read("pipeline.conf")

    account_id = parser.get("aws_config", "account_id")
    access_key = parser.get("aws_config", "access_key")
    secret_key = parser.get("aws_config", "secret_key")
    s3_bucket_name = parser.get("aws_config", "s3_bucket")


def new_s3_client():
    s3 = boto3.client(
        's3', aws_access_key_id=access_key, aws_secret_access_key=secret_key
    )

    return s3
