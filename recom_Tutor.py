from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

class TutorRecommendationSystem:
    def __init__(self, connector):
        self.connector = connector

    def retrieve_node_attributes(self, label):
        # Recupera los atributos de los nodos del tipo especificado
        query = f"MATCH (n:{label}) RETURN n.`Nombre Completo` AS NombreCompleto, n.Especialidad AS Especialidad"
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
            nombre = self.preprocess_text(item["NombreCompleto"])
            especialidad = self.preprocess_text(item["Especialidad"])

            processed_attributes.append({"NombreCompleto": nombre, "Especialidad": especialidad})
        return processed_attributes

    def run_recommendation(self):
        # Ejecuta el sistema de recomendación de tutorías

        # Cursos disponibles para tutorías
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

        print("Bienvenido al portal de tutorías")
        print("Cursos disponibles para tutorías:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")

        # Solicita al usuario que seleccione el curso en el que necesita ayuda
        course_index = int(input("Seleccione el número del curso en el que necesita ayuda: ")) - 1
        if course_index < 0 or course_index >= len(courses):
            print("Opción inválida. Inténtelo nuevamente.")
            self.run_recommendation()

        selected_course = courses[course_index]
        user_preferences = [selected_course]

        # Realiza las recomendaciones de tutores
        recommendations = self.recommend_items(user_preferences, "Tutor")

        print("Tutores recomendados:")
        for recommendation in recommendations:
            tutor = recommendation["NombreCompleto"]
            especialidad = recommendation["Especialidad"]
            print(f"Tutor: {tutor} - Especialidad: {especialidad}")

    def vectorize_attributes(self, attributes):
        # Vectoriza los atributos utilizando TF-IDF
        vectorizer = TfidfVectorizer()
        attributes_text = [item["NombreCompleto"] + " " + item["Especialidad"] for item in attributes]
        vectors = vectorizer.fit_transform(attributes_text)
        return vectors, vectorizer

    def calculate_similarity(self, user_preferences, attribute_vectors, vectorizer):
        # Calcula la similitud entre las preferencias del usuario y los atributos vectorizados
        user_preferences_text = " ".join(user_preferences)
        user_preferences_vector = vectorizer.transform([user_preferences_text])
        similarity_scores = cosine_similarity(user_preferences_vector, attribute_vectors)
        return similarity_scores

    def recommend_items(self, user_preferences, label):
        # Realiza las recomendaciones de tutores

        # Recupera los atributos de los nodos del tipo especificado
        attributes = self.retrieve_node_attributes(label)

        # Realiza el preprocesamiento de los atributos
        processed_attributes = self.preprocess_attributes(attributes)

        # Vectoriza los atributos
        attribute_vectors, vectorizer = self.vectorize_attributes(processed_attributes)

        # Calcula la similitud entre las preferencias del usuario y los atributos vectorizados
        similarity_scores = self.calculate_similarity(user_preferences, attribute_vectors, vectorizer)

        recommendations = []
        for index, item in enumerate(attributes):
            similarity_score = similarity_scores[0][index]
            recommendations.append({
                "NombreCompleto": item["NombreCompleto"],
                "Especialidad": item["Especialidad"],
                "Similarity": similarity_score
            })

        # Ordena las recomendaciones por similitud en orden descendente
        recommendations = sorted(recommendations, key=lambda x: x["Similarity"], reverse=True)
        return recommendations
