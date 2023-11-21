from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'taewrui',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'your_dag',
    default_args=default_args,
    description='Your DAG',
    schedule_interval=timedelta(hours=1),  # 주기적으로 실행하고자 하는 간격 설정
)

