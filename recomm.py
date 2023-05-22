from conexion import run_query

# Knowledge-based recommendation function


def recommend_knowledge_based(user_preferences):

    cypher_query = """
    MATCH (tutor:tutor)-[:TEACHES]->(subject:materia)
    WHERE subject.name IN {preferences}
    RETURN tutor as result
    UNION
    MATCH (resource:Resource)-[:ABOUT]->(subject:Subject)
    WHERE subject.name IN {preferences}
    RETURN resource as result
    """.format(preferences=user_preferences)

# User-based collaborative filtering function


def recommend_user_based(user_id):
    # Write a Cypher query to find similar users and what tutors/resources they like
    cypher_query = """
    MATCH (user:User)-[:LIKED]->(resource:Resource)<-[:LIKED]-(similarUser:User)
    WHERE user.id = {user_id} AND NOT (user)-[:LIKED]->(resource)
    RETURN resource
    """.format(user_id=user_id)

    results = run_query(cypher_query)
    return results

# Hybrid recommendation function


def recommend(user_preferences, user_id):
    knowledge_based_results = recommend_knowledge_based(user_preferences)
    user_based_results = recommend_user_based(user_id)

    # Here you'd combine the results from the two methods in a way that makes sense for your use case
    # This is just a simple example
    combined_results = list(set(knowledge_based_results + user_based_results))

    return combined_results


def main_menu():
    print("Bienvenido al portal de tutorias")
    print("1. Tutorias")
    print("2. Otro tipo")
    choice = input("elige una opción: ")

    if choice == '1':
        tutor_menu()
    elif choice == '2':
        other_resources_menu()
    else:
        print("Invalid option")
        main_menu()


def tutor_menu():
    print("Selecciona el tipo de tutorias:")
    print("1. Virtuales")
    print("2. Presenciales")
    option = input("Ingrese su opción: ")

    if option == "1":
        courses = [
            "Algoritmos y Programación Básica",
            "Programación Orientada a Objetos",
            "Programación de Microprocesadores",
            "Bases de Datos I",
            "Sistemas y Tecnologías Web"
        ]

        print("Cursos disponibles para tutorías virtuales:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")

        course_index = int(input("Seleccione el número del curso en el que necesita ayuda: ")) - 1
        if course_index < 0 or course_index >= len(courses):
            print("Opción inválida. Inténtelo nuevamente.")
            tutor_menu()

        selected_course = courses[course_index]

        # Call the recommendation function based on the selected course
        tutors = recommend_knowledge_based([selected_course])
        print("Tutors recomendados:")
        for tutor in tutors:
            print(tutor)

    elif option == "2":
        # Add logic for in-person tutoring
        pass

    else:
        print("Opción inválida. Inténtelo nuevamente.")

    main_menu()


def other_resources_menu():
    choice = input("Necesitas videos? (si/no): ")

    if choice.lower() == 'si':
        # Here, call the recommend function with the appropriate parameters
        from recomm import recommend_knowledge_based
        videos = recommend_knowledge_based(["Video Topic 1", "Video Topic 2"])  # Replace with actual video topics
        print("Recommended videos:", videos)
    else:
        # Here, call the recommend function with the appropriate parameters
        from recomm import recommend_knowledge_based
        other_resources = recommend_knowledge_based(["Non-Video Topic 1", "Non-Video Topic 2"])  # Replace with actual non-video topics
        print("Recommended resources:", other_resources)

# Run the menu
main_menu()

