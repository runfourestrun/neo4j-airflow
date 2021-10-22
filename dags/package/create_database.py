from package.connection import Neo4j

def create_database(**kwargs):
    db = Neo4j(username=kwargs.get('username'),password=kwargs.get('password'),database=kwargs.get('database'))
    q = '''
    :use Neo4j
    '''
    db.write(q)