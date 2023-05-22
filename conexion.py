from neo4j import GraphDatabase

uri = "neo4j+s://25a39f57.databases.neo4j.io"
user = "neo4j"
password = "NJ-2zgfqdrVnZ7RF_WK2-4ZjNgrWL6elIhXpuTbFrtg"

# Crea una sesión para interactuar con la base de datos
driver = GraphDatabase.driver(uri, auth=(user, password))

# Define una función para ejecutar una consulta
def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()

# Ejemplo de consulta
query = "MATCH (n) RETURN n LIMIT 5"
result = run_query(query)
print(result)

# Cierra la conexión al finalizar
driver.close()
