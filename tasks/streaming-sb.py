import requests
import json
import pandas as pd
import os
from datetime import datetime, timedelta
from google.cloud import storage

credentials_path = "/app/credentials.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

bucket_name = 'bucket-sb'


#수집 시점에서 1시간 전, timezone의 9시간 시차
time = datetime.now() + timedelta(hours=9) - timedelta(hours=1)
time_str = time.strftime("%Y-%m-%d/") + str(time.hour)
file_name = f'CycleRentData-{time_str.replace("/", "-")}.csv'

df = []
i = 0
while True:
    start_index = i*1000 +1
    end_index = (i+1)*1000
    url = f'http://openapi.seoul.go.kr:8088/596a58424d74616538376853696674/json/tbCycleRentData/{start_index}/{end_index}/{time_str}'
    js = requests.get(url).json()
    
    try: # 조회할 데이터가 없을 시 json의 구조가 다름
        js_parsed = js['rentData']['row']
        df.append(pd.DataFrame(js_parsed).drop(columns=['START_INDEX', 'END_INDEX', 'RNUM'], inplace=False))
        i += 1
    except:
        break

# 모두 병합하여 csv로 변환
df_concat = pd.concat(df, axis=0)
df_csv = df_concat.to_csv(index=False)

#Upload to GCS
client = storage.Client.from_service_account_json(credentials_path)
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(file_name)
blob.upload_from_string(df_csv, content_type='text/csv')



