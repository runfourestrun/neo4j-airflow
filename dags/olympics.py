from airflow import DAG
import neo4j
from airflow.providers.neo4j.operators.neo4j import Neo4jOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta,datetime
from package.create_database import create_database
from package.create_constraints import create_constraints
from package.load_athletes import load_athletes

default_args = {
    'owner': 'Alexander Fournier',
    'depends_on_past': False,
    'email': ['alexander.fournier@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
}






dag = DAG(
    dag_id='Neo4jOlympicsDemo',
    description='Pulling Tabular Olmypic Domain data and importing it into Graph',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
)



with dag:
    t1 = PythonOperator(
        task_id='create-db',
        python_callable=create_database,
        op_kwargs = {'username':'neo4j','password':'test','database':'system'},
        dag =dag,
    )
    
    t2 = PythonOperator(
        task_id='create_constrants',
        python_callable=create_constraints,
        op_kwargs = {'username':'neo4j','password':'Reddit123!','database':'system'},
        dag = dag,
    )


    t3 = PythonOperator(
        task_id='load_athletes',
        python_callable=load_athletes,
        op_kwargs = {'username':'neo4j','password':'Reddit123!','database':'system'},
        dag = dag,
    )


t2 >> t3
