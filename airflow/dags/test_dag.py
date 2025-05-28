from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv
import os

def write_hello_to_csv():
    file_path = "/opt/airflow/files/hello.csv"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["hello"])

with DAG(
    dag_id='test_dag',
    start_date=datetime(2025, 5, 23, 0, 0),  # Can be in the past
    schedule_interval=None,  # Disable automatic scheduling
    catchup=False,
    description='Triggered by GitHub Actions on merge to main',
) as dag:
    write_csv_task = PythonOperator(
        task_id='write_hello_to_csv',
        python_callable=write_hello_to_csv,
    )

