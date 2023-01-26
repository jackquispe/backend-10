## Crear el entorno virtual
```
python -m venv
```

## Activar el entorno virtual
```
venv\Scripts\activate
source venv/Scripts/activate
source venv/bin/activate
```

## Intslar Django
```
pip install Django
pip freeze > requirements.txt
```

## Crear nuestro proyecto
```
django-admin startproject django_intro
```

## Correr el servicio
```
cd django_intro
python manage.py runserver
```

## Migrar los modelos
```
python manage.py migrate
```

## Crear un superusuario
```
python manage.py createsuperuser
```
user: admin
pass: administrador