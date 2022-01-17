from airflow import DAG
import tempfile
import itertools as IT
import os

from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta



def print_path():
    return os.path.abspath(__file__)



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

dag = DAG('auto-scale',
          default_args=default_args,
          start_date=datetime(2022, 1, 11),
          schedule_interval=timedelta(days=1),
          catchup=False,
          tags=['example'])


t1 = BashOperator(
    task_id='task_1',
    bash_command='python3 /opt/airflow/OCI-AutoScale/AutoScaleALL.py',
    dag=dag)