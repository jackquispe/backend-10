from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from models.categorias_model import Categoria
# aca utilizaremos el archivo .env para agreegarlo a las variablesm de emtorno
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# inicializar la aplicaicon de SQLAlchemy con nuestra aplicaicon flask
conexion.init_app(app)

# este cointrolador se ejecutara antes del primer request de nuestro servidor
@app.before_first_request
def inicializadora():
    # realizar la creacion de datos los modelos de nuestro proyecto como tablas en las base de datos
    conexion.create_all()

if __name__ == '__main__':
    app.run(debug=True)