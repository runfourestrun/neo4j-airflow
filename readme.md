## Airflow to orchestrate personal Neo4j projects

![](https://github.com/runfourestrun/neo4j-airflow/blob/master/images/img.png)

Graphs to orchestrate:

* Olympics


## Problems:
* When I trigger a dag from airflow (which is hosted in a docker-compose - it is unable to connect to localhost database... 






## Neo4j Docker Image testing:

```
docker pull neo4j:latest -t neo-alexander-image


docker run \
    --name neo-alexander-image \
    -p 7474:7474 -p 7687:7687 \
    -d \
    -v $HOME/neo4j_docker_mounts/data:/data \
    -v $HOME/neo4j_docker_mounts/logs:/logs \
    -v $HOME/neo4j_docker_mounts/conf:/conf \
    --env NEO4J_AUTH=neo4j/test \
    neo4j:latest
```
