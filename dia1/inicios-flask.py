from flask import Flask

# si el archivo principal del proyecto su valor de la variable
# __name__ sera __main__ caso contrario sera None(vacio)
app = Flask(__name__)
# patron de diseño de software (Singleton)

# un decorador se usa con el '@' y sirve para modificar
# ciertp metodo de una clase sin la necesidad de modificaar el funcionamiento
# natural(es una modificacion parcial) luego de utilizar eld ecorador
# se crea una funcion que sera la nueva funcionalidad de ese metodo
@app.route('/')
def inicio():
    return 'Hola desde mi servidor de Flask'

# cada vez que modifiquemos algun archivo del proyecto y guardamos
app.run(debug=True) # sirve para ejecutrar