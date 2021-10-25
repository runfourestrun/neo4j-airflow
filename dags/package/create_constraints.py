from package.connection import Neo4j


def create_person_not_null_constraints(**kwargs):
    db = Neo4j(username=kwargs.get('username'),password=kwargs.get('password'),database=kwargs.get('database'))
    cypher = '''
    
    CREATE CONSTRAINT IF NOT EXISTS
    ON (p:Person)
    ASSERT p.name IS NOT NULL;
    
    '''
    db.write(cypher)

def create_person_unique_constraints(**kwargs):
    db = Neo4j(username=kwargs.get('username'), password=kwargs.get('password'), database=kwargs.get('database'))
    cypher = '''
        CREATE CONSTRAINT IF NOT EXISTS
        ON (p:Person)
        ASSERT p.name IS UNIQUE; '''

    db.write(cypher)


def create_country_not_null_constraint(**kwargs):
    db = Neo4j(username=kwargs.get('username'), password=kwargs.get('password'), database=kwargs.get('database'))

    cypher = '''
        CREATE CONSTRAINT IF NOT EXISTS
        ON (c:Country)
        ASSERT c.name IS NOT NULL;
        '''
    db.write(cypher)


def create_country_unique_constraints(**kwargs):
    db = Neo4j(username=kwargs.get('username'), password=kwargs.get('password'), database=kwargs.get('database'))
    cypher = '''
        CREATE CONSTRAINT IF NOT EXISTS
        ON (c:Country)
        ASSERT c.name IS UNIQUE;  
        '''
    db.write(cypher)


def create_sport_not_null_constraints(**kwargs):
    db = Neo4j(username=kwargs.get('username'), password=kwargs.get('password'), database=kwargs.get('database'))
    cypher = '''
        CREATE CONSTRAINT IF NOT EXISTS
        ON (s:Sport)
        ASSERT s.name IS NOT NULL;
        '''
    db.write(cypher)


def create_sport_unique_constraint(**kwargs):
    db = Neo4j(username=kwargs.get('username'), password=kwargs.get('password'), database=kwargs.get('database'))
    cypher = '''
        CREATE CONSTRAINT IF NOT EXISTS
        ON (s:Sport)
        ASSERT s.name IS UNIQUE;
        '''
    db.write(cypher)

    