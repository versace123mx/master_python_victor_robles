import suma #suma es el archivo suma.py y para utilizar el metodo seria suma.sumar(4,10)
from suma import sumar #suma es el archivo suma.py y sumar es el metodo

import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
print(current) 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
print(parent)
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

from restar.resta import restaBonito

print(f"La suma es {sumar(4,10)}")

print(f"La suma es {restaBonito(4,10)}")