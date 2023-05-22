from conexion import run_query

# Knowledge-based recommendation function
def recommend_knowledge_based(user_preferences):

    cypher_query = """
    MATCH (tutor:Tutor)-[:TEACHES]->(subject:Subject)
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
    print("Selecciona el tipo de tutorias")
    print("1. Virtuales")
    print("2. Presenciales")
    choice = input("elige una opción: ")

    year = input("¿Que año cursas actualmente? : ")
    semester = input("¿En que semestre te encuentras?: ")
    course = input("Ingresa el curso en el que necesitas apoyo: ")

    user_preferences = [type_of_tutoring, year, subject]

    # Now get the recommendations
    recommendations = recommend_knowledge_based(user_preferences)
    
    # Print the recommendations
    print("\nWe recommend the following tutors based on your preferences:")
    for tutor in recommendations:
        print(tutor)
    
    return

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

