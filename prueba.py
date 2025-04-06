import sys
import os

credencial = "GITHUB_TOKEN"
variable_entorno = os.getenv(credencial)
if variable_entorno is not None:
    with open("salida.txt","w") as archivo:
        archivo.write(str(variable_entorno))
else:
    with open("salida.txt","w") as archivo:
        archivo.write(f'Variable {credencial} no existe')
