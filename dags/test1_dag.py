from airflow import DAG
#from airflow.operators import BashOperator,PythonOperator

from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                  datetime.min.time())

default_args = {
    'owner': 'Julio Vasquez',
    'depends_on_past': False,
    'email' : ['julio.v.vasquez@oracle.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retry': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('simple',
          default_args=default_args,
          start_date=datetime(2022, 1, 11),
          schedule_interval=timedelta(days=1),
          catchup=False,
          tags=['example'])


t1 = BashOperator(
    task_id='test-airflow',
    bash_command='python3 ./scripts/create_files.py',
    dag=dag)
