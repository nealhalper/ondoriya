import requests
from minio import Minio
import io
import polars as pl
from config import BASE_URL, MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET_NAME, FILES_TO_INGEST

def upload_parquet_to_minio():
    minio_client = Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False
    )

    if not minio_client.bucket_exists(MINIO_BUCKET_NAME):
        minio_client.make_bucket(MINIO_BUCKET_NAME)

    for file_name in FILES_TO_INGEST:
        url = f"{BASE_URL}/{file_name}"
        response = requests.get(url)
        response.raise_for_status()

        df = pl.read_csv(io.BytesIO(response.content))
        parquet_buffer = io.BytesIO()
        df.write_parquet(parquet_buffer)
        parquet_buffer.seek(0)

        parquet_file_name = file_name.replace(".csv", ".parquet")
        minio_client.put_object(
            MINIO_BUCKET_NAME,
            parquet_file_name,
            parquet_buffer,
            parquet_buffer.getbuffer().nbytes
        )
        print(f"Uploaded {parquet_file_name} to Minio")

if __name__ == "__main__":
    upload_parquet_to_minio()