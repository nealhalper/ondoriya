import requests
from minio import Minio
import os
import io
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

MINIO_ENDPOINT = os.getenv("MINIO_EXTERNAL_URL")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")

FILES_TO_INGEST = [
    "faction_distribution.csv",
    "households.csv",
    "language_building_blocks.csv",
    "language_roots.csv",
    "moons.csv",
    "people.csv",
    "planets.csv",
    "region_biome.csv",
    "regions.csv"
]

def main():
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

        file_data = io.BytesIO(response.content)
        minio_client.put_object(
            MINIO_BUCKET_NAME,
                file_name,
                file_data,
                len(response.content)
        )
        print(f"Uploaded {file_name} to Minio")

if __name__ == "__main__":
    main()