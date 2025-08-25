import duckdb
from minio import Minio
import io
import polars as pl
from config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET_NAME, FILES_TO_INGEST, SQL_TEMPLATE

def ingest_parquet_to_duckdb():
    minio_client = Minio(
        MINIO_ENDPOINT,
        access_key=MINIO_ACCESS_KEY,
        secret_key=MINIO_SECRET_KEY,
        secure=False
    )

    con = duckdb.connect(r"D:\data\ondoriya\bronze.duckdb")

    for file_name in FILES_TO_INGEST:
        parquet_file = file_name.replace(".csv", ".parquet")
        response = minio_client.get_object(MINIO_BUCKET_NAME, parquet_file)
        parquet_data = io.BytesIO(response.read())
        df = pl.read_parquet(parquet_data)
        table_name = parquet_file.replace(".parquet", "")
        sql = SQL_TEMPLATE.format(table_name=table_name)
        con.execute(sql)

    con.close()
    print("All Parquet files ingested into bronze.duckdb")

if __name__ == "__main__":
    ingest_parquet_to_duckdb()