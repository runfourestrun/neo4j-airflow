from airflow import DAG
import neo4j
from airflow.providers.neo4j.operators.neo4j import Neo4jOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta,datetime
from connection import Neo4j
from create_databases import create_database

default_args = {
    'owner': 'Alexander Fournier',
    'depends_on_past': False,
    'email': ['alexander.fournier@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
}


connection_credentials = {username:'neo4j',password:'Reddit123!',database:'system'}

def create_database(**kwargs):
    print(kwargs['username'])


dag = DAG(
    dag_id='Neo4j-Olympics-Demo',
    description='Pulling Tabular Olmypic Domain data and importing it into Graph',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
)



with dag:
    t1 = PythonOperator(
        task_id='Create Database in Neo4j using a Python Operator',
        python_callable=create_database,
        op_kwargs = {username:'neo4j',password:'Reddit123!',database:'system'},
        dag =dag,
    )


t1
