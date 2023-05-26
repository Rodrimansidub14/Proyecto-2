### Proyecto 2 fase 2
# rodrigo mansilla
# ALGORITMOS Y ESTRUCTURAS DE DATOS

from neo4j import GraphDatabase



class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None

    def connect(self):
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def run_query(self, query, **kwargs):
        with self.driver.session() as session:
            result = session.run(query, **kwargs)
            records = list(result)
            return records
    
    
    def create_node(self, label, properties):
        properties_string = ", ".join([f"{k}: ${k}" for k in properties.keys()])
        query = f"CREATE (n:{label} {{{properties_string}}})"
        self.run_query(query, **properties)


    def delete_node(self, label, node_id):
        conditions = f"WHERE ID(n) = {node_id}"
        query = f"MATCH (n:{label}) {conditions} DELETE n"
        self.run_query(query)


    def create_relationship(self, start_node, end_node, relationship_type, properties=None):
        query = f"MATCH (a) WHERE ID(a) = {start_node} MATCH (b) WHERE ID(b) = {end_node} CREATE (a)-[:{relationship_type} {properties}]->(b)"
        self.run_query(query)

    def delete_relationship(self, start_node, end_node, relationship_type):
        query = f"MATCH (a)-[r:{relationship_type}]->(b) WHERE ID(a) = {start_node} AND ID(b) = {end_node} DELETE r"
        self.run_query(query)