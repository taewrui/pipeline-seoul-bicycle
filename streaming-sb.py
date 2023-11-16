import requests
import json
import pandas as pd
import os
from google.cloud import storage

credentials_path = "/app/delta-discovery-405105-1010a9d46e53.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

bucket_name = 'bucket-sb'
file_name = 'CycleRentData.csv'

url = 'http://openapi.seoul.go.kr:8088/596a58424d74616538376853696674/json/tbCycleRentData/1/100/2023-11-16/9'
res = requests.get(url)
js = res.json()


df = pd.DataFrame(js['rentData']['row'])
df_csv = df.to_csv(index=False)

client = storage.Client.from_service_account_json(credentials_path)
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(file_name)
blob.upload_from_string(df_csv, content_type='text/csv')



