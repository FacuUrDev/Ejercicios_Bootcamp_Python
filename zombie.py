# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 04:05:30 2022

@author: Blacktooth
"""
#AMBIENTE
class Zombie():
    def __init__(self,salud):
        self.salud=salud
    def __str__(self):
        return "Salud: {}".format( self.salud )
    def Gritar(self):
        print('Argggg')
    def Sabe_correr(self):
         False
    def sin_vida(self):
        self.salud==0
    def recibir_danio(self,puntos):
        self.salud = max (self.salud - puntos * 2, 0)
    
class SuperZombie(Zombie):
    def Sabe_correr(self):
        True
    def recibir_danio(self,puntos):
        self.salud = max (self.salud - puntos * 3, 0)

    def regenerarse(self):
        self.salud = 200



class Persona():#clase abstracta
    def energia(self,energia):
        self.energia=energia
    def __str__(self):
        return "Energia: {}".format( self.energia )
    def atacar(self,zombi, danio):
        zombi.recibir_danio (danio)
        
  
class Sobreviviente(Persona):
        def __init__(self):
            self.energia = 1000
     
        def beber(self):
            self.energia *= 1.25
   

class Aliado(Persona):
        def __init__(self):
            self.energia = 500
                        
        def beber(self):
            self.energia *= 1.10
  
        def atacar(self,zombi, danio):
            zombi.recibir_danio (danio)
            self.energia *= 0.95
# bloque principal
# creamos el nuevo objeto, lo inicializamos y se imprime
# bloque principal
# creamos el nuevo objeto, lo inicializamos y se imprime
kiki=Zombie(100)
buba = SuperZombie(200)
print(kiki)
print(buba)
roger=Sobreviviente()
eli=Aliado()

print(roger)
print(eli)
