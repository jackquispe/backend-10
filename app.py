from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from flask_migrate import Migrate


from models.categorias_model import Categoria
from models.productos_model import Producto

# aca utilizaremos el archivo .env para agreegarlo a las variablesm de emtorno
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')



# inicializar la aplicaicon de SQLAlchemy con nuestra aplicaicon flask
conexion.init_app(app)

# Inicializamos la clase migrate pasandole nuestra aplicaicon de flask y nuestra conexion a SQLAlchemy
Migrate(app, conexion)



# Asi utilizariamos la creacion de las tablas sin utilizar migraciones
# este cointrolador se ejecutara antes del primer request de nuestro servidor
@app.before_first_request
def inicializadora():
    # realizar la creacion de datos los modelos de nuestro proyecto como tablas en las base de datos
    # conexion.create_all()
    pass

if __name__ == '__main__':
    app.run(debug=True)