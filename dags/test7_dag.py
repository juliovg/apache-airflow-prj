from airflow import DAG
#from airflow.operators import BashOperator,PythonOperator
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

dag = DAG('test7',
          default_args=default_args,
          start_date=datetime(2022, 1, 11),
          schedule_interval=timedelta(days=1),
          catchup=False,
          tags=['example'])

#t1 = BranchPythonOperator(
#         task_id="task_1",
#         python_callable=print_path)


t1 = BashOperator(
        task_id='task_1',
        bash_command='python3 /scripts/create_files.py',
        dag=dag)
#
#
# t3 = BashOperator(
#     task_id='test-airflow',
#     bash_command='python3 ~/dags/scripts/create_files.py',
#     dag=dag)

#t1 >> t2 #>> t3
