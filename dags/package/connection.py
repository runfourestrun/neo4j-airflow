from neo4j import GraphDatabase, Query, unit_of_work


class Neo4j():
    """
    Neo4J DB Interface class
    """

    def __init__(self, *args, **kwargs):
        url = kwargs.get('url', 'bolt://neo4j:7687/')
        username = kwargs.get('username', 'neo4j')
        password = kwargs.get('password', 'Reddit123!')
        database = kwargs.get('database', 'neo4j')
        self.client = GraphDatabase.driver(url, auth=(username, password), database=database)

    @unit_of_work(timeout=1200)
    def __run(self, tx, query, **kwargs):
        if kwargs.get('data_frame'):
            return pd.DataFrame([dict(record) for record in tx.run(query)])
        result = [row for row in tx.run(query)]
        return result

    def execute(self, query, **kwargs):
        with self.client.session() as session:
            tx = session.begin_transaction()
            result = self.__run(tx, query, **kwargs)
            tx.close()
            return result

    def read(self, query, **kwargs):
        with self.client.session() as session:
            return session.read_transaction(self.__run, query, **kwargs)

    def write(self, query):
        with self.client.session() as session:
            return session.write_transaction(self.__run, query)