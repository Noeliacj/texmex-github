#!/usr/bin/python3
import sys

with open ('recetas.md' , 'r') as fichero:
    x=fichero.read()

    print(x)

sys.exit(0)

