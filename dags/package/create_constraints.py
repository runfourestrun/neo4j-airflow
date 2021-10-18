from package.connection import Neo4j


def create_constraints(**kwargs):
    db = Neo4j(username=kwargs.get('username'),password=kwargs.get('password'),database=kwargs.get('database'))
    cypher = '''
    :USE olympics1;
    
    CREATE CONSTRAINT IF NOT EXISTS
    ON (p:Person)
    ASSERT p.name IS NOT NULL;

    CREATE CONSTRAINT IF NOT EXISTS
    ON (p:Person)
    ASSERT p.name IS UNIQUE;

    CREATE CONSTRAINT IF NOT EXISTS
    ON (c:Country)
    ASSERT c.name IS NOT NULL;

    CREATE CONSTRAINT IF NOT EXISTS
    ON (c:Country)
    ASSERT c.name IS UNIQUE;

    CREATE CONSTRAINT IF NOT EXISTS
    ON (s:Sport)
    ASSERT s.name IS NOT NULL;

    CREATE CONSTRAINT IF NOT EXISTS
    ON (s:Sport)
    ASSERT s.name IS UNIQUE;
    '''
    dw.write(cypher)
    