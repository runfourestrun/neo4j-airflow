# Airflow to orchestrate personal Neo4j projects

![](https://github.com/runfourestrun/neo4j-airflow/blob/master/images/img.png)



Prepare the environment: 

airflow docker-compose pulled from here: https://airflow.apache.org/docs/apache-airflow/2.0.1/start/docker.html


1. Create volumes for airflow:
* $AIRFLOW_HOME/confg
* $AIRFLOW_HOME/dags
* $AIRFLOW_HOME/logs
3. Create volumes for Neo4j: 
* $HOME/neo4j_docker_mounts/conf
* $HOME/neo4j_docker_mounts/data
* $HOME/neo4j_docker_mounts/logs

4. Copy neo4j.conf to $HOME/neo4j_docker_mounts/conf

2. Pull latest neo4j enterprise image and run it


```

docker run \
    --name neo-alexander-image \
    -p 7474:7474 -p 7687:7687 \
    -d \
    -v $HOME/neo4j_docker_mounts/data:/data \
    -v $HOME/neo4j_docker_mounts/logs:/logs \
    -v $HOME/neo4j_docker_mounts/conf:/conf \
    --env NEO4J_AUTH=neo4j/test \
    --env NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    neo4j:enterprise
    
  
```



3. Run 
```
docker-compose up airflow-init
```

4. Run 
```
docker-compose up
```


## Graphs to orchestrate:

* Olympics


## Problems:
* When I trigger a dag from airflow (which is hosted in a docker-compose - it is unable to connect to localhost database... 




