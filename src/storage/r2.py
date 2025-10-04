import boto3
from src.env import get_settings

settings = get_settings()

r2_client = boto3.client(
    "s3",
    endpoint_url=f"https://{settings.r2_account_id}.r2.cloudflarestorage.com",
    aws_access_key_id=settings.r2_access_key_id,
    aws_secret_access_key=settings.r2_secret_access_key,
    region_name="auto",
)


def upload_file(file_name: str, content: bytes, content_type: str) -> str:
    bucket = settings.r2_bucket_name
    r2_client.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=content,
        ContentType=content_type,
        ACL="public-read",
    )
    return f"{settings.r2_public_base}/{file_name}"
