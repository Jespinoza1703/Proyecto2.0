# Clase Barra:
# Atributos:
# ancho
# largo
# x
# y
#######################
# Metodos:
# get_y()
# posicionar()
# mover()
import pygame
import os

#Objeto Barra/Paleta
class Barra:
	def __init__(self,x,y,largo,valor):
		self.ancho = 1
		self.largo = largo
		self.x = x
		self.y = y
		self.valor = valor

	def get_y(self):
		return self.y

	# Dibuja la barra en la matriz
	def posicionar(self,matriz):
		for n in range(self.largo):
			matriz[self.y+n][self.x] = self.valor

	# Mueve la barra por la matriz y evita que se salga de la misma.
	def mover(self,vy,matriz):
		if vy == -1 and self.y + self.largo < 25:
			matriz[self.y][self.x] = 0
			self.y -= vy
			matriz[self.y][self.x] = self.valor
		elif vy == 1 and self.y > 0:
			matriz[self.y + self.largo - 1][self.x] = 0
			self.y -= vy
			matriz[self.y][self.x] = self.valor
