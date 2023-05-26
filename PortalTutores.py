from conexion import Neo4jConnector
from recom_Tutor import TutorRecommendationSystem
from recom_Recurso import ResourceRecommendationSystem

uri = "neo4j+s://d4df5c4f.databases.neo4j.io"
user = "neo4j"
password = "IMLUq1wL99_9UKqOmRLaZBLbdFw041QHqgu5_U-_VTo"

connector = Neo4jConnector(uri, user, password)
connector.connect()

def display_main_menu():
        # Función principal que muestra el menú y maneja las opciones del usuario

    while True:
        print("########################################")
        print("########################################")
        print("########################################")
        print("########  ####    #####  ##.    ########")
        print("########  ####  #  ###  #  #############")
        print("########  ####  ##  #  ##  ###   #######")
        print("########       ####   ####       #######")
        print("########################################")
        print("########################################")
        print("===================================")
        print("Bienvenido al portal de recomendaciones")
        print("===================================")
        print("1. Tutorías")
        print("2. Recursos")
        print("3. Agregar información")
        print("4. Eliminar información")
        print("5. Salir")
        print("-----------------------------------")

        
        choice = input("Elige una opción: ")

        if choice == '1':
            run_tutor_recommendation()
        elif choice == '2':
            run_resource_recommendation()
        elif choice == '3':
            add_info(connector)
        elif choice == '4':
            del_info(connector)
        elif choice == '5':
            break
        else:
            print("Opción inválida. Inténtelo nuevamente.")

    connector.close()

    
    
# Función para agregar nueva información a la base de datos
def add_info(connector):
    print("Agregar nueva información:")
    name = input("Nombre: ")
    specialty = input("Especialidad: ")
    courses = input("Cursos (separados por comas): ").split(",")

    properties = {
        "name": name,
        "specialty": specialty,
        "courses": courses
    }

    connector.create_node("Tutor", properties)
    print("Nueva información agregada exitosamente.")


# Función para eliminar información de la base de datos
def del_info(connector):
    node_id = input("ID del nodo a eliminar: ")
    connector.delete_node("Tutor", node_id)
    print("Información eliminada exitosamente.")


    # Función para ejecutar el sistema de recomendación de tutorías
def run_tutor_recommendation():
    recommendation_system = TutorRecommendationSystem(connector)
    recommendation_system.run_recommendation()

    # Función para ejecutar el sistema de recomendación de recursos
def run_resource_recommendation():
    recommendation_system = ResourceRecommendationSystem(connector)
    recommendation_system.run_recommendation()

def main():
    display_main_menu()

if __name__ == "__main__":
    main()
