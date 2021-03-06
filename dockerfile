FROM apache/airflow:2.2.0


RUN pip install --no-cache-dir neo4j==4.3.4  \
    && pip install --no-cache-dir boto3==1.18.60 \
    && pip install apache-airflow-providers-neo4j==2.0.1




# COPY dags/test.py /opt/airflow/dags
# COPY config/airflow.cfg /opt/airflow/config
