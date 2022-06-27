# Entrega1-Battaglino,Sanchez
 # Entrega intermedia del proyecto final
1.- Instalar django con el siguiente comando:
  python pip install django
  python -m pip install django

2.- Aplicar modelos de BD y migraciones
  comando --> python manage.py makemigrations
  comando --> python manage.py migrate

3.- Crear usuario administrador, el mismo solicita nombre usuario, correo electronico (opcional) y contraseña.
  comando --> python manage.py createsuperuser

4.- Iniciar servidor
  comando --> python manage.py runserver
  
5.- Abrir el navegador 
  url --> http://127.0.0.1:8000/
  
6.- Descripcion pestañas de pagina:
    6.1.- Inicio = Muestra los 3 ultimos registros almacenados en la BD de Cursos y Profesores, con opcion de filtrar los 3 registros (Cursos, Profesores y               Alumnos).
    6.2.- Cursos = Observar todos los cursos disponibles, permite la creacion de un nuevo curso y la opcion de filtrar cursos.
    6.3.- Profesores = Observar todos los profesores registrados, permite el registro de nuevo profesor y la opcion de filtrar profesores.
    6.4.- Alumnos = Observar todos los alumnos registrados, permite el registro de nuevo alumno y la opcion de filtrar alumnos. 

----------------------------------------------------------------------------------------------------------------------------------------------
# Para poder ingresar al Panel de Administracion
1.a.- Ingresar al navegador de preferencia y colocar la siguiente url:
      --> http://127.0.0.1:8000/admin
  b.- Ingresar con el usuario y contraseña creada en el punto 3.
  c.- En la siguiente ventana se podran observar las diferentes tablas creadas para la aplicacion.
