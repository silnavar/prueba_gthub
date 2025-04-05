import sys
import os

variable_entorno = os.getenv("CREDENTIALS_GC")
with open("salida.txt","w") as archivo:
  archivo.write(variable_entorno)
