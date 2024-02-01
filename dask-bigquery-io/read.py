
import dask.dataframe as dd
from dask_bigquery import BigQueryTable
from dask.distributed import Client
from google.cloud import bigquery

# # Create a BigQueryTable object
# table = BigQueryTable(project_id, dataset_id, table_name)

# # Read the BigQuery table as a Dask DataFrame
# df = table.to_dask()

# # Print the first few rows of the DataFrame
# print(df.head())
project_id = 'bigquery-public-data'
dataset_id = 'openaq'
table_id = 'global_air_quality'

# SQL query to select all columns from the table
sql_query = f'SELECT * FROM `{project_id}.{dataset_id}.{table_id}`'

# Set up Dask BigQuery reader
bq_reader = dd.read_bigquery(sql_query, project_id=project_id, dataset_id=dataset_id, table_id=table_id)

# Display Dask DataFrame
print(bq_reader.head())
