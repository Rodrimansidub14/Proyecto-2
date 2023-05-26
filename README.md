# Documentación del código

## Clase Neo4jConnector

La clase `Neo4jConnector` proporciona métodos para establecer la conexión con una base de datos Neo4j y ejecutar consultas en ella.

### Métodos

- `__init__(self, uri, user, password)`: Constructor de la clase `Neo4jConnector`. Recibe como parámetros la URI de la base de datos Neo4j, el nombre de usuario y la contraseña para la autenticación.

- `connect(self)`: Establece la conexión con la base de datos Neo4j.

- `close(self)`: Cierra la conexión con la base de datos Neo4j.

- `run_query(self, query, **kwargs)`: Ejecuta una consulta en la base de datos Neo4j. Recibe como parámetro la consulta Cypher en forma de cadena. Los argumentos adicionales son utilizados para proporcionar parámetros a la consulta.

- `create_node(self, label, properties)`: Crea un nuevo nodo con la etiqueta especificada y las propiedades dadas.

- `delete_node(self, label, conditions)`: Elimina los nodos que cumplen con las condiciones especificadas.

- `create_relationship(self, start_node, end_node, relationship_type, properties=None)`: Crea una relación entre dos nodos con el tipo y las propiedades especificadas.

- `delete_relationship(self, start_node, end_node, relationship_type)`: Elimina la relación entre dos nodos con el tipo especificado.

## Clase TutorRecommendationSystem

La clase `TutorRecommendationSystem` proporciona un sistema de recomendación de tutores basado en la especialidad y los cursos solicitados.

### Métodos

- `__init__(self, connector)`: Constructor de la clase `TutorRecommendationSystem`. Recibe como parámetro una instancia de `Neo4jConnector` para interactuar con la base de datos.

- `retrieve_node_attributes(self, label)`: Recupera los atributos de los nodos que tienen la etiqueta especificada.

- `preprocess_text(self, text)`: Realiza el preprocesamiento de un texto, eliminando puntuación, convirtiendo a minúsculas y eliminando espacios en blanco.

- `preprocess_attributes(self, attributes)`: Realiza el pre-procesamiento de los atributos recuperados de los nodos.

- `run_recommendation(self)`: Ejecuta el sistema de recomendación de tutores.

- `vectorize_attributes(self, attributes)`: Convierte los atributos de los tutores en vectores utilizando TF-IDF.

- `calculate_similarity(self, user_preferences, attribute_vectors, vectorizer)`: Calcula la similitud entre las preferencias del usuario y los atributos de los tutores utilizando la similitud del coseno.

- `recommend_items(self, user_preferences, label)`: Realiza las recomendaciones de tutores en función de las preferencias del usuario.

## Clase ResourceRecommendationSystem

La clase `ResourceRecommendationSystem` proporciona un sistema de recomendación de recursos basado en los cursos seleccionados.

### Métodos

- `__init__(self, connector)`: Constructor de la clase `ResourceRecommendationSystem`. Recibe como parámetro una instancia de `Neo4jConnector` para interactuar con la base de datos.

- `retrieve_node_attributes(self, label)`: Recupera los atributos de los nodos que tienen la etiqueta especificada.

- `preprocess_text(self, text)`: Realiza el preprocesamiento de un texto


## Uso del sistema de recomendaciones

1. Instalación:
    
    - Tener Python instalado en tu computadora.
    - Instala las bibliotecas necesarias ejecutando el siguiente comando en la terminal: `pip install scikit-learn neo4j`.
2. Requisitos de la computadora:
    
    - Se requiere una conexión a internet para acceder a la base de datos Neo4j.
    - Se recomienda tener suficiente memoria RAM disponible para ejecutar las operaciones de procesamiento de texto y cálculo de similitud.
3. Configuración de la base de datos:
    
    - Asegúrate de tener una base de datos Neo4j en funcionamiento y con los datos correspondientes.
    - Actualiza los parámetros `uri`, `user` y `password` en el código para que coincidan con la configuración de tu base de datos.
4. Uso del sistema de recomendaciones:
    
    - Crea una instancia de `Neo4jConnector` proporcionando los parámetros de conexión.
    - Crea una instancia de `TutorRecommendationSystem` o `ResourceRecommendationSystem` pasando la instancia de `Neo4jConnector`.
    - Llama al método `run_recommendation()` en la instancia creada para obtener las recomendaciones correspondientes.

Requisitos del Sistema 
Python 3.x instalado .
Acceso a Internet para descargar las bibliotecas y recursos necesarios.
Cuenta en Neo4j para configurar la base de datos de grafos.
Pasos de Instalación
Instalar Python: Si no tienes Python instalado, visita el sitio web oficial de Python (https://www.python.org) y descarga la versión más reciente compatible con tu sistema operativo. Sigue las instrucciones de instalación para configurar Python en tu computadora.

Configurar entorno virtual (opcional): Se recomienda crear un entorno virtual para el proyecto. Abre una terminal y navega hasta la ubicación del proyecto. Ejecuta el siguiente comando para crear un entorno virtual:

Copy code
python -m venv venv
Luego, activa el entorno virtual ejecutando el comando correspondiente según tu sistema operativo:

En Windows:

Copy code
venv\Scripts\activate
En macOS y Linux:

bash
Copy code
source venv/bin/activate
Instalar dependencias: Asegúrate de que estás en el directorio raíz del proyecto (donde se encuentra el archivo requirements.txt). Ejecuta el siguiente comando para instalar las dependencias necesarias:

Copy code
pip install -r requirements.txt
Esto instalará las bibliotecas requeridas, como neo4j, scikit-learn, entre otras.

Configurar base de datos de Neo4j: Crea una cuenta en Neo4j (https://neo4j.com) y sigue las instrucciones para configurar una base de datos de grafos. Anota la URI, el nombre de usuario y la contraseña de tu base de datos, ya que se utilizarán en la configuración.

Configurar la conexión a Neo4j: Abre el archivo conexion.py en un editor de texto. En la sección de inicialización de Neo4jConnector, actualiza los valores de uri, user y password con la información de tu base de datos de Neo4j.

Ejecutar el programa.


python PortalTutores.py
El programa se ejecutará y se mostrará un menú con opciones para acceder a las tutorías, recursos y agregar/eliminar información.
