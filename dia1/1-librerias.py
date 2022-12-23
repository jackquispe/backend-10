# unaVariable -> camelCase
# UnaVariable -> PascalCase
# una_variable -> snake_Case

# Para desinstalar utilizamos -> pip uninstall camelcase



from camelcase import CamelCase

instancia = CamelCase()

texto = 'hola yo deberia esta camel'

resultado = instancia.hump(texto)

print(resultado)

# venv -> virtual enviroment : entorno virtual
# -m -> modulo interno de python -m --module
