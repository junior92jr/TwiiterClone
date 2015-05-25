# TwiiterClone
Clone of Twitter


Debe tener Instalado
---------------------
pip
virtualenv



Instalar Requerimientos
-------------------------------
1) Clonar la carpeta del repositorio 

2) A la carpeta clonada, ejecutar en la terminal
	$ virtualenv TwitterClone

3) Aplicar el comando para activar la carpeta virtual
	$ source bin/activate

4) Instalar los requerimientos de la carpeta requeriments.txt
   	$ pip install -r requeriments.txt
   Es equivalente a hacer lo siguiente:
	$ pip install Django==1.7
	$ pip install pillow

5) Se esta usando por defecto SLQlite que viene incorporado a Django, Dentro de la Carpeta TwitterClone aplicar el siguiente comando:
	$ python manage.py migrate

6) Ya se tiene todo listo para correr la aplicacion.


Correr la Aplicacion
---------------------------
1) Dentro de la carpeta del proyecto ejecutar el comando:
	$ python manage.py createsuperuser
        <poner los datos y contraseñas>
2)Para correr la aplicacion
	$ python manage.py runserver

3) En el Browser de preferencia GoogleChrome (tiene mejor desenpeño con -webkit-) 
   correr el     127.0.0.1:8000/twitterclone/

4) Si se desea se puede correr en 2 o 3 Browsers simultaneos con diferentes usuarios.

Usar la Aplicacion
--------------------
1) Registra tu usuario (se puede entrar con el superuser previamente creado)
2) logeate
3) Puedes añadir tweets con "Add Tweet", se puede postear Imagenes y Url, aca se hay 2 urls que contienen imagenes en ellas:
	 
         http://www.esotech.org/wp-content/uploads/2011/12/jquery_logo.png
         http://www.linuxtrent.it/sites/default/files/images/drupal-logo.jpg
 
