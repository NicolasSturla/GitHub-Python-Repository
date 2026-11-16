# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:54:15 2022

@author: Nicolas
"""

# CLASS INHERITANCE:
    
# una clase puede heredar atributos o metodos de otra, para no tener que 
# escribirla toda de 0 de nuevo.
# para hacer esto, al definir una clase se agrega entre parentesis otra clase 
# de la cual se van a herear rasgos:
    
class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, Exale.")
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print("doing this underwater.")
        
# esta linea lo que hace es llamar a la funcion breathe de la super clase y 
# agregarles cosas especicias para fish.
# Cabe aclarar que el metodo breathe ya estaba incluido cuando usamos el 
# metodo super en la inicializacion, pero dejarlo solo ahi hace que no sea 
# posible agregarle lineas extras a dicho metodo solo para fish
    
    def swim(self):
        print("moving in water.")
 
# donde super hace referencia a la super clase. 

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)