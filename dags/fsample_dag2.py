from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'codetops',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet():
    print("Hello World ")



def get_integrate():
    print("Sample Data Integration")
   

def get_manipulate():
    print("Data Manipuulation")


with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v1',
    description='Our first dag using python operator',
    start_date=datetime(2021, 10, 6),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
    )

    task2 = PythonOperator(
        task_id='get_integrate',
        python_callable=get_integrate
    )

    task3 = PythonOperator(
        task_id='get_manipulate',
        python_callable=get_manipulate
    )

    [task2, task3] >> task1