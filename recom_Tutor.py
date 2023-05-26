from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

class TutorRecommendationSystem:
    def __init__(self, connector):
        self.connector = connector

    def retrieve_node_attributes(self, label):
        query = f"MATCH (n:{label}) RETURN n.`Nombre Completo` AS NombreCompleto, n.Especialidad AS Especialidad"
        return self.connector.run_query(query)

    def preprocess_text(self, text):
        if text is None:
            return ""

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Convert to lowercase
        text = text.lower()

        # Remove leading/trailing white spaces
        text = text.strip()

        return text

    def preprocess_attributes(self, attributes):
        processed_attributes = []
        for item in attributes:
            nombre = self.preprocess_text(item["NombreCompleto"])
            especialidad = self.preprocess_text(item["Especialidad"])

            processed_attributes.append({"NombreCompleto": nombre, "Especialidad": especialidad})
        return processed_attributes

    
    def run_recommendation(self):
        
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

        course_index = int(input("Seleccione el número del curso en el que necesita ayuda: ")) - 1
        if course_index < 0 or course_index >= len(courses):
            print("Opción inválida. Inténtelo nuevamente.")
            self.run_recommendation()

        selected_course = courses[course_index]
        user_preferences = [selected_course]

        recommendations = self.recommend_items(user_preferences, "Tutor")

        print("Tutores recomendados:")
        for recommendation in recommendations:
            tutor = recommendation["NombreCompleto"]
            especialidad = recommendation["Especialidad"]
            print(f"Tutor: {tutor} - Especialidad: {especialidad}")


    def vectorize_attributes(self, attributes):
        vectorizer = TfidfVectorizer()
        attributes_text = [item["NombreCompleto"] + " " + item["Especialidad"] for item in attributes]
        vectors = vectorizer.fit_transform(attributes_text)
        return vectors, vectorizer

    def calculate_similarity(self, user_preferences, attribute_vectors, vectorizer):
        user_preferences_text = " ".join(user_preferences)
        user_preferences_vector = vectorizer.transform([user_preferences_text])
        similarity_scores = cosine_similarity(user_preferences_vector, attribute_vectors)
        return similarity_scores

    def recommend_items(self, user_preferences, label):
        attributes = self.retrieve_node_attributes(label)
        processed_attributes = self.preprocess_attributes(attributes)

        attribute_vectors, vectorizer = self.vectorize_attributes(processed_attributes)
        similarity_scores = self.calculate_similarity(user_preferences, attribute_vectors, vectorizer)

        recommendations = []
        for index, item in enumerate(attributes):
            similarity_score = similarity_scores[0][index]
            recommendations.append({
                "NombreCompleto": item["NombreCompleto"],
                "Especialidad": item["Especialidad"],
                "Similarity": similarity_score
            })

        recommendations = sorted(recommendations, key=lambda x: x["Similarity"], reverse=True)
        return recommendations

 