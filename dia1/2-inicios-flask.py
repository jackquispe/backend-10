from flask import Flask, request
from flask_cors import CORS

# si el archivo principal del proyecto su valor de la variable
# __name__ sera __main__ caso contrario sera None(vacio)
app = Flask(__name__)
# patron de diseño de software (Singleton)

# un decorador se usa con el '@' y sirve para modificar
# ciertp metodo de una clase sin la necesidad de modificaar el funcionamiento
# natural(es una modificacion parcial) luego de utilizar eld ecorador
# se crea una funcion que sera la nueva funcionalidad de ese metodo

# Ahora configuramos nuestro CORS (control de acceso de recursos cruzados)
# origins = '*' -> permite todos los origenes
# methods = '*' -> permite todos los metodos
CORS(app=app, origins=['http://127.0.0.1:5500'], methods=['GET', 'POST'])

usuarios =[
    {
        'nombre': 'Eduardo',
        'apellido': 'Juares'
    },
    {
        'nombre': 'Juana',
        'apellido': 'Rosriguez'
    },
    {
        'nombre': 'Eduardo',
        'apellido': 'Castillo'
    } 
]

@app.route('/')
def inicio():
    return 'Hola desde mi servidor de Flask'


@app.route('/mostrar-hora', methods=['GET','POST'])
def mostrarHora():
   
    
    # CONTROLLER (controlador ) es la funcionalidad que se ralizara dentro de in determiando endpoint
    # request -> me dara toda la informaicon que viene del cliente
    print(request.method)
    if request.method == 'GET':
        return{
            'content': 'Me hiciste GET'
        }
    elif request.method == 'POST':
        return {
            'content': 'Me hiciste POST'
        }
         # no se suele retornar strings (cadena de texto) sino se utiliza diccionarios
    return {
        'content': '22:50:15'
    }

@app.route('/usuarios', methods =['GET', 'POST'])
def gestionUsuario():
    if request.method == 'GET':
        return {
            'message': 'Los usuarios son',
            'content': usuarios
        }
    elif request.method == 'POST':
        # agregar un nuevo usuario
        # get.json convierte el body entrante en un diccionario
        # desde un json
        print(request.get_json())
        data=request.get_json()
        usuarios.append(data)
        return {
            'message': 'Usuario agregado exitosamemte'
        }

# cada vez que modifiquemos algun archivo del proyecto y guardamos
app.run(debug=True) # sirve para ejecutrar