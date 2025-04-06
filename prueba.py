import sys
import os

credencial = "GITHUB_TOKEN"
variable_entorno = os.getenv(credencial)
if credencial in locals():
    print(variable_entorno)
    with open("salida.txt","w") as archivo:
        archivo.write(variable_entorno)
else:
    with open("salida.txt","w") as archivo:
        archivo.write(f'Variable {credencial} no existe')
