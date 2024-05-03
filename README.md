# API RESTful con Flask y MongoDB
## Introducción
Este proyecto implementa una API RESTful utilizando Flask como framework de Python y MongoDB como base de datos NoSQL. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una colección de libros.
Herramientas utilizadas

- Flask: Framework de Python para desarrollar aplicaciones web.
- MongoDB Atlas: Servicio de base de datos en la nube de MongoDB.
- Postman: Herramienta para probar y documentar APIs.

## Funcionalidades
La API proporciona los siguientes endpoints:

- POST /books: Crea un nuevo libro en la colección.
- GET /books: Obtiene la lista de todos los libros en la colección.
- GET /books/<id>: Obtiene un libro específico por su ID.
- PUT /books/<id>: Actualiza la información de un libro existente.
- DELETE /books/<id>: Elimina un libro de la colección.

## Desarrollo
El proyecto utiliza las siguientes dependencias:

- flask
- flask_pymongo
- python-dotenv

La conexión con MongoDB Atlas se realiza a través de una URI proporcionada en una variable de entorno. Los datos de los libros se almacenan en una colección llamada books dentro de una base de datos llamada maindb.
Conclusiones

MongoDB facilitó el desarrollo del proyecto gracias a su interfaz intuitiva y bien documentada.
Se creó una base de datos maindb y una colección books para almacenar la información de los libros.
El servicio gratuito de MongoDB Atlas proporciona 512MB de almacenamiento y está respaldado por dos réplicas en AWS para garantizar la integridad de los datos.

## Bibliografía

¿Qué es una API de RESTful? - Explicación de API de RESTful - AWS
