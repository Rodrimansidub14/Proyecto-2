from neo4j import GraphDatabase

uri = "neo4j+s://2028f15f.databases.neo4j.io:7687/"
user = "neo4j"
password = "XWQCC9vxf-0U8l_HR1p3OId4t2jrVjaErQTjRlJP518"

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
