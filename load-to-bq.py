from google.cloud import bigquery
from google.cloud import storage
import os
#
credentials_path = "/app/credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

project_id = 'delta-discovery-405105'
dataset_id = 'dataset_cycle'
table_id = 'RentCycle'

bucket_name = 'bucket-sb'
file_name = 'CycleRentData.csv'

bigquery_client = bigquery.Client.from_service_account_json(credentials_path)
storage_client = storage.Client.from_service_account_json(credentials_path)

table_ref = bigquery_client.dataset(dataset_id).table(table_id)
table = bigquery_client.get_table(table_ref)

job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1  
job_config.autodetect = True  

uri = f"gs://{bucket_name}/{file_name}"
load_job = bigquery_client.load_table_from_uri(uri, table_ref, job_config=job_config)
load_job.result()  

print(f"File {file_name} loaded into {table_id}.")