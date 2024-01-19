import logging
import os

import boto3

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

ENDPOINT_URL = os.environ["ENDPOINT_URL"]
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
BUCKET_NAME = os.environ["BUCKET_NAME"]

TEST_FILE_PATH = "assets/sample.pdf"


def perform_s3_test():
    s3 = boto3.client(
        "s3",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    logger.info(f'Uploading file "{TEST_FILE_PATH}" to S3 bucket "{BUCKET_NAME}".')
    s3.upload_file(TEST_FILE_PATH, BUCKET_NAME, os.path.basename(TEST_FILE_PATH))
    logger.info(
        f'File "{TEST_FILE_PATH}" uploaded successfully to S3 bucket "{BUCKET_NAME}".'
    )

    # List objects in the bucket
    response = s3.list_objects(Bucket=BUCKET_NAME)
    logger.info(f'Listing keys in S3 bucket "{BUCKET_NAME}"')
    for obj in response.get("Contents", []):
        logger.info(obj["Key"])


if __name__ == "__main__":
    perform_s3_test()
