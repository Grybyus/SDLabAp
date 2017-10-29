# SDLabAp
Requisitos:
- Ubuntu(Mate o 14.4)
- python 2.7
- virtualenv 15.1.0
- Django 1.11.2
- django-materialize-css 0.0.1
- postgresql 9.5.9
- psycopg2 2.7.1

(asumimos instalado Python, pip y Virtualenv)

Pasos de Instalación:
- Iniciar un entorno virtual nuevo con Python 2.7 y su pip respectivo
- Instalar django: sudo pip install Django==1.11.2
- Instalar conector a postgresql: sudo pip install psycopg2
- Instalar BD: sudo apt-get install postgresql
- Instalar materialize: sudo pip install django-materialize-css
- Redirijase a la carpeta Data
- Cree un nuevo usuario en Postgresql
psql -U postgres -h localhost -W
CREATE USER <<Ingrese nombre de usuario aquí>> PASSWORD '<<Ingrese su pass>>';
ALTER ROLE <<Ingrese nombre de usuario>> WITH SUPERUSER;
- Cree una nueva Base de datos en Postgresql llamada "distribuidos"
CREATE DATABASE distribuidos WITH OWNER <<Ingrese nombre de usuario>>;
GRANT ALL PRIVILEGES ON DATABASE distribuidos TO <<Ingrese nombre de usuario>>;
- Ejecute los siguientes comandos:
- psql -h localhost -d distribuidos -U <<USUARIO DE SU BD>> -p 5432 -a -f crearTablas.sql
- psql -h localhost -d distribuidos -U <<USUARIO DE SU BD>> -p 5432 -a -f insertarDatosDefinitivo.sql
- Ctrl + Z
- muevase hasta la carpeta SDin y modifique el archivo settings.py en las llaves de DATABASES
  Cambie el usuario, y la password con las suyas.
- muevase a la carpeta inicial del proyecto (donde esta el archivo manage.py) y ejecute
python manage.py runserver
- finalmente abra el link que aparece en la consola en su navegador preferido.

Detalles:
* Se utilizo el LOCALHOST para la BD
* La aplicación desde el Frontend donde se realiza la consulta, y se envia al Backend el cual termina por consultar a la Base de datos
comunicandose por el conector psycopg2 y así entregar este resultado hasta el Frontend
