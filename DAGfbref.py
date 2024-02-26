import datetime
from airflow import DAG 
from airflow.operators.bash import BashOperator

default_args = {"retries": 2 }

dag = DAG('fbgr_data_scraping', start_date= datetime.datetime(2023, 4, 7), default_args=default_args, schedule= '@daily')

fbref_scraping_task = BashOperator( task_id='fbref_scraping_task', bash_command='python fbref_scraping.py', dag=dag )