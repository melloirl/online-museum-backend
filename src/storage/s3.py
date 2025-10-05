import boto3
from src.env import get_settings

settings = get_settings()

s3_client = boto3.client(
    "s3",
    endpoint_url=settings.s3_endpoint_url,
    aws_access_key_id=settings.s3_access_key_id,
    aws_secret_access_key=settings.s3_secret_access_key,
    region_name="auto",
)


def upload_file(file_name: str, content: bytes, content_type: str) -> str:
    bucket = settings.s3_bucket_name
    s3_client.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=content,
        ContentType=content_type,
        ACL="public-read",
    )
    return f"{settings.s3_public_base}/{file_name}"
