from neo4j import GraphDatabase
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ResourceRecommendationSystem:
    def __init__(self, connector):
        self.connector = connector

    def retrieve_node_attributes(self, label):
        # Recupera los atributos de los nodos del tipo especificado
        query = f"MATCH (n:{label}) RETURN n.r AS Recurso, n.Materias AS Cursos" # ¿query = f"MATCH (n:{label}) RETURN n.Recurso AS Recurso, n.Cursos AS Cursos"?
        return self.connector.run_query(query)

    def preprocess_text(self, text):
        # Realiza el preprocesamiento del texto
        if text is None:
            return ""

        # Elimina la puntuación
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Convierte a minúsculas
        text = text.lower()

        # Elimina espacios en blanco al inicio y al final
        text = text.strip()

        return text

    def preprocess_attributes(self, attributes):
        # Realiza el preprocesamiento de los atributos
        processed_attributes = []
        for item in attributes:
            recurso = self.preprocess_text(item["Recurso"])
            cursos = self.preprocess_text(item["Cursos"])

            processed_attributes.append({"Recurso": recurso, "Cursos": cursos})
        return processed_attributes

    def run_recommendation(self):
        # Ejecuta el sistema de recomendación de recursos

        courses = [
            "Cálculo 1",
            "Interacción Humano-Computador",
            "Organización de Computadoras y Assembler",
            "Programación de Microprocesadores",
            "Sistemas y Tecnologías Web",
            "Programación Orientada a Objetos",
            "Bases de Datos I",
            "Física 1",
            "Algoritmos y Programación Básica",
            "Programación de Plataformas Móviles",
            "Algoritmos y Estructuras de Datos"
        ]

        print("Bienvenido al portal de recursos")
        input("Presiona cualquier tecla para continuar.")

        print("Cursos disponibles para recursos:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")

        course_index = int(input("Seleccione el número del curso para el que necesita recursos: ")) - 1
        if course_index < 0 or course_index >= len(courses):
            print("Opción inválida. Inténtelo nuevamente.")
            self.run_recommendation()

        selected_course = courses[course_index]

        # Realiza las recomendaciones de recursos
        recommendations = self.recommend_items([], "Recurso", selected_course)

        print("Recursos recomendados:")
        for recommendation in recommendations:
            resource = recommendation["Recurso"]
            print(f"Recurso: {resource} - Curso: {selected_course}")

    def recommend_items(self, user_preferences, label, selected_course):
        # Realiza las recomendaciones de recursos

        # Recupera los atributos de los nodos del tipo especificado
        attributes = self.retrieve_node_attributes(label)

        # Realiza el preprocesamiento de los atributos
        processed_attributes = self.preprocess_attributes(attributes)

        # Filtra los recursos que corresponden al curso seleccionado
        matching_resources = [resource for resource in processed_attributes if selected_course in resource["Cursos"]]

        if matching_resources:
            print("Recursos recomendados:")
            for resource in matching_resources:
                print(f"Recurso: {resource['Recurso']}")
        else:
            print("No se encontraron recursos para el curso seleccionado.")

        return matching_resources
