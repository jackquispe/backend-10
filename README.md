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

## Crar una app
```
python manage.py startapp "nombre_app"
```

## Registramos nuestra app en settings.py > INSTALLED_APPS 

```python
INSTALLED_APPS = [
    .....
    'almacen'
]
```

## Crear nuestro model y migrar
```
python manage.py makemigrations
python manage.py migrate
```

## Luego de esto instalamos Django Rest Framework
```
pip install djangorestframework
```

## Agregar DRF a INSTALLED_APPS
```
settings > INSTALLED_APPS
.....
'rest_framework',
```

## Documentar nuestra API con swagger y Redoc
```
pip install drf-yasg
```

## Configurar `drf-yasg`
```

```