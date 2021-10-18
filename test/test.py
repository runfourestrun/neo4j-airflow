from package.create_database import create_database


connection_credentials = {'username':'neo4j','password':'Reddit123!','database':'system'}


create_database(**connection_credentials)