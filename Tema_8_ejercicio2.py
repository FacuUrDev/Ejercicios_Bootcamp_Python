from pickle import *

class Vehiculo:

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return self.color + " " + self.puertas


corsa = Vehiculo("rojo", "5")
print(clio)

file = open('vehiculo_objeto', 'w+b')

dump(clio, file)

file.seek(0)
nuevo_clio = load(file)

print(nuevo_clio)
file.close()
