import sys
import os

variable_entorno = os.getenv("GITHUB_TOKEN")
with open("salida.txt","w") as archivo:
  archivo.write(variable_entorno)
