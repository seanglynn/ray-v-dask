import dask.dataframe as dd
from google.cloud import bigquery
from google.cloud import storage
import pickle

def write_dask_dataframe_to_bigquery(dataframe, table_name, project_id, dataset_id):
    client = bigquery.Client(project=project_id)
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
    job_config.create_disposition = bigquery.CreateDisposition.CREATE_IF_NEEDED

    dataframe.to_parquet('/tmp/temp.parquet')
    table_ref = f"{project_id}.{dataset_id}.{table_name}"
    job = client.load_table_from_parquet('/tmp/temp.parquet', table_ref, job_config=job_config)
    job.result()

    print(f"Dask dataframe written to BigQuery table: {table_ref}")

def write_dask_dataframe_to_gcs(dataframe, bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)

    dataframe.to_csv('/tmp/temp.csv', index=False)
    blob.upload_from_filename('/tmp/temp.csv')

    print(f"Dask DataFrame written to GCS: gs://{bucket_name}/{file_name}")

def write_dask_dataframe_to_pickle(dataframe, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(dataframe, f)

    print(f"Dask DataFrame written to pickle file: {file_path}")
