# Clase Bola:
# Atributos:
# x
# y
# direccion
# derecha
# vx
# vy
# socre1
# score2
#######################
# Metodos:
# mover()
# get_score1()
# get_score2()
# set_score1()
# set_score2()
# get_x()
# get_y()

import random
import pygame
import os

#Objeto Bola
class Bola:
	def __init__(self,x,y,direccion,derecha):
		self.x = x
		self.y =y
		self.vx = 1
		self.vy = 1
		self.direccion = direccion
		self.derecha = derecha
		self.score1 = 0
		self.score2 = 0

	def get_score1(self):
		return self.score1

	def get_score2(self):
		return self.score2

	def set_score1(self, new_score):
		self.score1 = new_score

	def set_score2(self, new_score):
		self.score2 = new_score

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def mover(self, matriz):
		# se mueve primero en las filas y luego en las columnas
		# Poner en negro el cuadro anterior
		matriz[self.y][self.x] = 0 
		# Cuando llegua abajo, cambie de direccion hacia arriba
		if self.y == 24 and self.direccion == -1: 
			self.direccion = 1
		# Cuando llegue arriba, cambie de direccion hacia abajo
		elif self.y == 0 and self.direccion == 1: 
			self.direccion = -1
		# Si llega al borde derecho y el cuadrado de matriz es negro, punto para jugador 1
		elif self.x == 37 and matriz[self.y][self.x + 1] == 0: 
			pygame.mixer.Sound(os.path.join('sounds', 'fail.wav')).play()
			self.derecha = False
			# Saque inicial direccion aleatorio
			self.direccion = random.randrange(-1, 2) 
			self.score1 += 1
			self.x = 20
			self.y = 12
		# Si llega al final y el siguiente es blanco, rebote
		elif self.x == 37 and matriz[self.y][self.x + 1] == 1: 
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			# Si paleta es mayor a 9
			if matriz[self.y - 6][self.x + 1] == 1 or matriz[self.y + 6][self.y + 1] == 1:
				print("WWWERTYULFDSAZVBN;MNBFDSDUIKJHAZXCV;SO")
				if matriz[self.y - 5][self.x + 1] == 0:
					self.direccion = random.randrange(-1, 2)
					self.derecha = False
				elif matriz[self.y + 1][self.x + 1] == 0:
					self.direccion = random.randrange(-1, 2)
					self.derecha = False
				else:
					self.direccion = random.randrange(-1, 2)
					self.derecha = False
			# Revisa si paleta es de 3
			if matriz[self.y - 3][self.x + 1] == 0 and matriz[self.y + 3][self.x + 1] == 0: 
				if matriz[self.y - 1][self.x + 1] == 0:
					self.direccion = 1
					self.derecha = False
				elif matriz[self.y + 1][self.x + 1] == 0:
					self.direccion = -1
					self.derecha = False
				else:
					self.direccion = 0
					self.derecha = False
			# Si paleta es 6
			if matriz[self.y - 3][self.x + 1] == 1 or matriz[self.y + 3][self.x + 1] == 1: 
				if matriz[self.y - 2][self.x + 1] == 0:
					self.direccion = 1
					self.derecha = False
				elif matriz[self.y + 2][self.x + 1] == 0:
					self.direccion = -1
					self.derecha = False
				else:
					self.direccion = 0
					self.derecha = False
			# Si paleta es 9
			if matriz[self.y - 5][self.x + 1] == 1 or matriz[self.y + 5][self.x + 1] == 1: 
				if matriz[self.y - 3][self.x + 1] == 0:
					self.direccion = 1
					self.derecha = False
				elif matriz[self.y + 3][self.x + 1] == 0:
					self.direccion = -1
					self.derecha = False
				else:
					self.direccion = 0
					self.derecha = False
		# Si llega a la barra doble derecha y el siguiente es blanco, rebote
		elif self.x == 29 and matriz[self.y][self.x + 1] == 1: 
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			# Revisa si paleta es de 3
			if matriz[self.y - 3][self.x + 1] == 0 and matriz[self.y + 3][self.x + 1] == 0: 
				if matriz[self.y - 1][self.x + 1] == 0:
					self.direccion = 1
					self.derecha = False
				elif matriz[self.y + 1][self.x + 1] == 0:
					self.direccion = -1
					self.derecha = False
				else:
					self.direccion = 0
					self.derecha = False
			# Si paleta es 6
			if matriz[self.y - 3][self.x + 1] == 1 or matriz[self.y + 3][self.x + 1] == 1: 
				if matriz[self.y - 2][self.x + 1] == 0:
					self.direccion = 1
					self.derecha = False
				elif matriz[self.y + 2][self.x + 1] == 0:
					self.direccion = -1
					self.derecha = False
				else:
					self.direccion = 0
					self.derecha = False
			# Si paleta es 9
			if matriz[self.y - 5][self.x + 1] == 1 or matriz[self.y + 5][self.x + 1] == 1: 
				if matriz[self.y - 3][self.x + 1] == 0:
					self.direccion = 1
					self.derecha = False
				elif matriz[self.y + 3][self.x + 1] == 0:
					self.direccion = -1
					self.derecha = False
				else:
					self.direccion = 0
					self.derecha = False

		# Si llega al principio y el siguiente cuadro es negro, rebote
		elif self.x == 2 and matriz[self.y][self.x -1] == 0: 
			pygame.mixer.Sound(os.path.join('sounds', 'fail.wav')).play()
			# Si llega al borde izquierdo, cambie de direccion hacia derecha
			self.derecha = True 
			# Saque inicial direccion aleatoria
			self.direccion = random.randrange(-1, 2) 
			self.score2 += 1
			self.x = 20
			self.y = 12
		# Si llega al principio y el siguiente es blanco
		elif self.x == 2 and matriz[self.y][self.x -1] == 1: 
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			# Revisa si paleta es de 3
			if matriz[self.y - 3][self.x - 1] == 0 and matriz[self.y + 3][self.x - 1] == 0: 
				if matriz[self.y - 1][self.x - 1] == 0:
					self.direccion = 1
					self.derecha = True
				elif matriz[self.y + 1][self.x - 1] == 0:
					self.direccion = -1
					self.derecha = True
				else:
					self.direccion = 0
					self.derecha = True
			# Si paleta es 6
			if matriz[self.y - 3][self.x - 1] == 1 or matriz[self.y + 3][self.x - 1] == 1: 
				if matriz[self.y - 2][self.x - 1] == 0:
					self.direccion = 1
					self.derecha = True
				elif matriz[self.y + 2][self.x - 1] == 0:
					self.direccion = -1
					self.derecha = True
				else:
					self.direccion = 0
					self.derecha = True
			# Si paleta es 9
			if matriz[self.y - 5][self.x - 1] == 1 or matriz[self.y + 5][self.x - 1] == 1: 
				if matriz[self.y - 3][self.x - 1] == 0:
					self.direccion = 1
					self.derecha = True
				elif matriz[self.y + 3][self.x - 1] == 0:
					self.direccion = -1
					self.derecha = True
				else:
					self.direccion = 0
					self.derecha = True
		# Si llega a la paleta doble izquierda y el siguiente es blanco
		elif self.x == 10 and matriz[self.y][self.x -1] == 1: 
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			# Revisa si paleta es de 3
			if matriz[self.y - 3][self.x - 1] == 0 and matriz[self.y + 3][self.x - 1] == 0: 
				if matriz[self.y - 1][self.x - 1] == 0:
					self.direccion = 1
					self.derecha = True
				elif matriz[self.y + 1][self.x - 1] == 0:
					self.direccion = -1
					self.derecha = True
				else:
					self.direccion = 0
					self.derecha = True
			# Si paleta es 6
			if matriz[self.y - 3][self.x - 1] == 1 or matriz[self.y + 3][self.x - 1] == 1: 
				if matriz[self.y - 2][self.x - 1] == 0:
					self.direccion = 1
					self.derecha = True
				elif matriz[self.y + 2][self.x - 1] == 0:
					self.direccion = -1
					self.derecha = True
				else:
					self.direccion = 0
					self.derecha = True
			# Si paleta es 9
			if matriz[self.y - 5][self.x - 1] == 1 or matriz[self.y + 5][self.x - 1] == 1: 
				if matriz[self.y - 3][self.x - 1] == 0:
					self.direccion = 1
					self.derecha = True
				elif matriz[self.y + 3][self.x - 1] == 0:
					self.direccion = -1
					self.derecha = True
				else:
					self.direccion = 0
					self.derecha = True
		# Si derecha es true, o sea, hacia la derecha
		if self.derecha == True: 
			if self.direccion == -1:
				self.x += self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				#print(1)
				#print('direccion: '+str(self.direccion))
				#print('derecha: '+str(self.derecha))
				#print('x: '+str(self.x))
				#print('y: '+str(self.y))
				#print('score1: '+str(self.score1))
				#print('score2: '+str(self.score2))
			elif self.direccion == 1:
				self.x += self.vx
				self.y -= self.vy 
				#print(2)
				#print('direccion: '+str(self.direccion))
				#print('derecha: '+str(self.derecha))
				#print('x: '+str(self.x))
				#print('y: '+str(self.y))
				#print('score1: '+str(self.score1))
				#print('score2: '+str(self.score2))
				matriz[self.y][self.x] = 1
			elif self.direccion == 0:
				self.x += self.vx
				matriz[self.y][self.x] = 1
				#print(3)
				#print('direccion: '+str(self.direccion))
				#print('derecha: '+str(self.derecha))
				#print('x: '+str(self.x))
				#print('y: '+str(self.y))
				#print('score1: '+str(self.score1))
				#print('score2: '+str(self.score2))
		# Si derecha es false, o sea hacia la izquierda
		elif self.derecha == False and self.x > 0: 
			if self.direccion == -1:
				self.x -= self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				#print(4)
				#print('direccion: '+str(self.direccion))
				#print('derecha: '+str(self.derecha))
				#print('x: '+str(self.x))
				#print('y: '+str(self.y))
				#print('score1: '+str(self.score1))
				#print('score2: '+str(self.score2))
			elif self.direccion == 1:
				self.x -= self.vx
				self.y -= self.vy 
				#print(5)
				#print('direccion: '+str(self.direccion))
				#print('derecha: '+str(self.derecha))
				#print('x: '+str(self.x))
				#print('y: '+str(self.y))
				#print('score1: '+str(self.score1))
				#print('score2: '+str(self.score2))
				matriz[self.y][self.x] = 1
			elif self.direccion == 0:
				self.x -= self.vx
				matriz[self.y][self.x] = 1
				#print(6)
				#print('direccion: '+str(self.direccion))
				#print('derecha: '+str(self.derecha))
				#print('x: '+str(self.x))
				#print('y: '+str(self.y))
				#print('score1: '+str(self.score1))
				#print('score2: '+str(self.score2))
