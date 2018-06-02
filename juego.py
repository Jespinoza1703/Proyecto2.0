import pygame
from tkinter import *
from tkinter import messagebox
from barra import Barra
from bola import Bola
from barra_doble import Barra_doble
import time
import random
import os

BLACK = (0,0,0)
WHITE = (255,255,255)
L = 20



# Constantes
ANCHO = 800
LARGO = 500

TIEMPO_NIVEL1 = 0.1
TIEMPO_NIVEL2 = 0.07
TIEMPO_NIVEL3 = 0.04

TAMAÑO_BARRA_1 = 9
TAMAÑO_BARRA_2 = 6
TAMAÑO_BARRA_3 = 3
TAMAÑO_BARRA_PRACTICA = 25


	


	

# Clase Juego:
# Atributos:
# pantalla
# matriz: [[],[],...,[]]
# score: int
# bola: Class
# nivel: int
# barra1: Class
# barra2: Class
# modo: str
# versus: str
#######################
# Metodos:
# crearMatriz()
# dibujarMatriz()
# cpu()
# jugar()
# dibujar()
pygame.init()
class Juego:
	def __init__(self, modo, nivel, versus, ventana, tamaño=None, time=TIEMPO_NIVEL1):
		self.pantalla = pygame.display.set_mode((ANCHO,LARGO))
		pygame.display.set_caption("Pong")
		self.FILAS = 30
		self.COLUMNAS = 40
		self.matriz = []
		self.crearMatriz()
		self.score = 0
		self.bola = Bola(20,12, random.randrange(-1, 2), True)
		self.nivel = nivel
		self.modo = modo
		self.versus = versus
		self.CPU = 0
		self.tamaño = tamaño
		self.time = time
		self.ventana = ventana

		# Se define el tiempo, tamaño de barra, modo y versus de cada nivel
		if self.nivel == 1:
			if self.time == None:
				self.tiempo = TIEMPO_NIVEL1
			else: 
				self.tiempo = time
				if self.modo == "Single":
					if self.tamaño == None:
						self.barra1 = Barra(1,2,TAMAÑO_BARRA_1) 
						self.barra2 = Barra(38,2,TAMAÑO_BARRA_1)
					else:
						# Si se le define un tamaño es porque está en modo práctica
						self.barra1 = Barra(1,2,self.tamaño) 
						self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA)
					if self.versus == "humano":
						self.CPU = 0
					elif self.versus == "cpu":
						self.CPU = 1
				else:
					# La primer barra es la de la izquiera, la otra la de la derecha
					if self.tamaño == None:
						self.barra1 = Barra_doble(1,2,9,13,TAMAÑO_BARRA_1)
						self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_1)
					else:
						self.barra1 = Barra_doble(1,2,9,13,self.tamaño) 
						self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA)
					if self.versus == "humano":
						# Si se escoje "humano" no se llama la función cpu()
						self.CPU = 0
					elif self.versus == "cpu":
						self.CPU = 1


	# Se crea auna matriz binaria(compuesta por ahora por 0s), de 25 filas x 40 columnas
	def crearMatriz(self):
		for i in range(self.FILAS):
			fila = []
			for j in range(self.COLUMNAS):
				# Llena la lista de ceros
				fila.append(0)
			self.matriz.append(fila)

	# Se va dibujando la matriz cuadro pr cuadro y se plasma en la pantalla
	def dibujarMatriz(self):
		for fila in range(self.FILAS):
			for columna in range(self.COLUMNAS):
				if self.matriz[fila][columna] == 0:
					# Si el cierta posición de la matriz hay un 0, se pinta de color negro
					pygame.draw.rect(self.pantalla, BLACK, [L* columna,L * fila,L,L])
				else:
					# Si el cierta posición de la matriz hay un 0, se pinta de color blanco
					# Esto es para la bola y las barras
					pygame.draw.rect(self.pantalla, WHITE, [L* columna,L * fila,L,L])
		# Define cada cuánto tiempo se va a actualizar la matriz
		time.sleep(self.tiempo)
		# Sibuja una línea blanca en medio de la pantalla
		pygame.draw.line(self.pantalla, WHITE, [ANCHO//2, 0], [ANCHO//2,LARGO], 4)

	# Barra controlada por la computadora
	def cpu(self):
		# La posicion en x de la bola es mayor a 28
		if self.bola.get_x() > 28:
			if self.bola.get_y() > self.barra2.get_y():
			# Si la posición en y de la bola es mayor que la de la barra
			# se mueve la barra hacia arriba o abajo siguiendo la bola
				self.barra2.mover(-1, self.matriz)
			else:
				self.barra2.mover(1, self.matriz)

	def jugar(self):
		global ventana
		fuera_juego = False
		# Genera múltiples eventos pygame.KEYDOWN
		pygame.key.set_repeat(50, 50)
		while not fuera_juego:
			# Si el score de alguno de los jugadores es igual a 5
			clock = pygame.time
			if self.versus != "practica":
				if self.bola.get_score1() == 5 or self.bola.get_score2() == 5:
					# Se reinician los scores
					self.bola.set_score1(0)
					self.bola.set_score2(0)
					# Se pasa de nivel
					self.nivel += 1	
					# Si pierde en el nivel 3, vuelve al nivel 1
					if self.nivel == 4:
						print("TIME: " + str(clock.get_ticks()/1000))
						self.archivarTiempos()
						pygame.quit()
					# Se limpia la matriz para dibujar las barras del siguiente nivel
					self.matriz = []
					# Se vuelve a crear la matriz
					self.crearMatriz()
					# Se definen las condiciones de acuerdo con cada nivel
					if self.nivel == 1:
						self.tiempo = TIEMPO_NIVEL1
						if self.modo == "Single":
							self.barra1 = Barra(1,2,TAMAÑO_BARRA_1) 
							self.barra2 = Barra(38,2,TAMAÑO_BARRA_1)
						else:
							self.barra1 = Barra_doble(1,2,9,13,TAMAÑO_BARRA_1)
							self.barra2 = Barra_doble(38,12,32,3,TAMAÑO_BARRA_1)

					elif self.nivel == 2:
						self.tiempo = TIEMPO_NIVEL2
						if self.modo == "Single":
							self.barra1 = Barra(1,2,TAMAÑO_BARRA_2) 
							self.barra2 = Barra(38,2,TAMAÑO_BARRA_2)
						else:
							self.barra1 = Barra_doble(1,2,9,13,TAMAÑO_BARRA_2)
							self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_2)

					elif self.nivel == 3:
						self.tiempo = TIEMPO_NIVEL3
						if self.modo == "Single":
							self.barra1 = Barra(1,2,TAMAÑO_BARRA_3) 
							self.barra2 = Barra(38,2,TAMAÑO_BARRA_3)
						else:
							self.barra1 = Barra_doble(1,2,9,13,TAMAÑO_BARRA_3)
							self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_3)


					
			else:
				if self.bola.get_score1() == 100:
					# Se reinician los scores
					self.bola.set_score1(0)
					# Se pasa de nivel
					self.nivel += 1
					# Se limpia la matriz para dibujar las barras del siguiente nivel
					self.matriz = []
					# Se vuelve a crear la matriz
					self.crearMatriz()
					if self.nivel == 1:
						self.tiempo = self.time
						if self.tamaño != None:
							if self.modo == "Single":
								self.barra1 = Barra(1,2,self.tamaño) 
								self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA)
							else:
								self.barra1 = Barra_doble(1,3,9,13,self.tamaño)
								self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA)

			# Eventos de las teclas
			for event in pygame.event.get():
				if event.type == pygame.QUIT: #is le da X, cierra todo
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN: #al presionar una tecla
					if event.key == pygame.K_UP:
						self.barra2.mover(1,self.matriz)
					elif event.key == pygame.K_DOWN:
						self.barra2.mover(-1,self.matriz)
					elif event.key == pygame.K_w:
						self.barra1.mover(1,self.matriz)
					elif event.key == pygame.K_s:
						self.barra1.mover(-1,self.matriz)
					elif event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()
					elif event.key == pygame.K_p:
						self.pausa()
					elif event.key == pygame.K_SPACE:
						self.ventana.deiconify()
						pygame.quit()

			# Aquí se actualiza constántemente la matriz para que
			# ocurra el movimiento de forma continua
			self.dibujarMatriz()

			self.dibujar()

			# se llama la función cpu solo si la variable CPU es igual a 1
			if self.CPU == 1:
				self.cpu()
	
			
	def dibujar(self):
		# Se defne un texto para poner en la pantalla
		font = pygame.font.Font(None, 100)
		score1 = self.bola.get_score1()
		score_text = font.render(str(score1), True,
								 (WHITE))
		# Se coloca el texto en la pantalla
		self.pantalla.blit(score_text, (150, 0))
		score2 = self.bola.get_score2()
		score_text2 = font.render(str(score2), True,
								 (WHITE))
		self.pantalla.blit(score_text2, (620, 0))
		# Coloca la bola en la matriz
		self.bola.mover(self.matriz)
		# Posiciona las barras en la matriz
		self.barra1.posicionar(self.matriz)
		self.barra2.posicionar(self.matriz)
		pygame.display.update()

	def archivarTiempos(self):	
		def abrirArchivo(archivo, modo): #abre el archivo
			file = open(archivo, modo)
			return file

		def separarTiempos(i):
			if i == len(listaTiempos):
				return
			listaTiempos[i] = listaTiempos[i].replace("\n", "").split(";")
			separarTiempos(i + 1)
		archivo = abrirArchivo("Tiempos.txt", "r")
		listaTiempos = archivo.readlines()
		separarTiempos(0)
		archivo.close()
		def crearVentana(): #Abre una nueva ventana donde hay dos botones: Administrar Apps y Administrar Vendedores
			vent = Tk()
			vent.title("Mejores Tiempos de Juego")
			vent.minsize (800, 500)
			canvas1 = Canvas (vent, width = 800, height = 500)
			canvas1.place (x = -1, y = -1)

			def volver():
				vent.destroy()
				self.ventana.deiconify()
			boton = Button (vent, font = ("arial", 12), width = 6, command = volver)
			boton.place (x = 120, y = 10)
			vent.mainloop()
		pygame.quit()
		crearVentana()

	def pausa(self):
		pausado = True
		
		while pausado:
			pantalla = pygame.display.set_mode((ANCHO,LARGO))
			font = pygame.font.Font(None, 25)
			for x in range (self.FILAS):
				score_text = font.render(str(self.matriz[x]), True,(WHITE))
				# Se coloca el texto en la pantalla
				pantalla.blit(score_text, (20, 20*x))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT: #is le da X, cierra todo
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN: #al presionar una tecla
					if event.key == pygame.K_p:
						pausado = False
