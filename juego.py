import pygame
from tkinter import *
from tkinter import messagebox
from barra import Barra
from barra_doble import Barra_doble
from bola import Bola
import time
import random
import os
import serial

#Puerto serial de Arduino
ser = serial.Serial('/dev/cu.itead-DevB', 9600, timeout=0)
#ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=0)

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
L = 20

# Constantes
ANCHO = 800
LARGO = 500

TIEMPO_NIVEL1 = 0.1
TIEMPO_NIVEL2 = 0.1
TIEMPO_NIVEL3 = 0.1

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

contador_colores = 0
total = None

class Juego:
	def __init__(self,trampolin, modo, nivel, versus, ventana, tamaño=None, time=TIEMPO_NIVEL1):
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
		self.trampolin = trampolin
		self.trampolin1 = Barra(10,5,4,2)
		self.trampolin2 = Barra(30,15,4,2)
		self.trampolin3 = Barra(20,10,4,2)
		self.musicOn = 1
		self.musicSpeed = 1
		self.background_color = (0, 0, 0)

		self.playMusic()

		# Se define el tiempo, tamaño de barra, modo y versus de cada nivel
		if self.nivel == 1:
			if self.time == None:
				self.tiempo = TIEMPO_NIVEL1
			else: 
				self.tiempo = time
				if self.modo == "Single":
					if self.tamaño == None:
						self.barra1 = Barra(1,2,TAMAÑO_BARRA_1,1) 
						self.barra2 = Barra(38,2,TAMAÑO_BARRA_1,1)
					else:
						# Si se le define un tamaño es porque está en modo práctica
						self.barra1 = Barra(1,2,self.tamaño,1) 
						self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA,1)
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
						self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA,1)
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
					pygame.draw.rect(self.pantalla, self.background_color, [L* columna,L * fila,L,L])
				elif self.matriz[fila][columna] == 2:
					# Si el cierta posición de la matriz hay un 0, se pinta de color negro
					pygame.draw.rect(self.pantalla, GREEN, [L* columna,L * fila,L,L])
				else:
					# Si el cierta posición de la matriz hay un 0, se pinta de color blanco
					# Esto es para la bola y las barras
					pygame.draw.rect(self.pantalla, WHITE, [L* columna,L * fila,L,L])
		# Define cada cuánto tiempo se va a actualizar la matriz
		time.sleep(self.time)
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
		global ventana, total, total1, total2, total3
		fuera_juego = False
		# Genera múltiples eventos pygame.KEYDOWN
		pygame.key.set_repeat(50, 50)
		inicial = time.time()
		while not fuera_juego:
			# Si el score de alguno de los jugadores es igual a 5
			if self.versus != "practica":
				if self.bola.get_score1() == 5 or self.bola.get_score2() == 5:
					# Se reinician los scores
					self.bola.set_score1(0)
					self.bola.set_score2(0)
					# Se pasa de nivel
					self.nivel += 1
					self.musicSpeed += 1
					self.playMusic()
					# Si pierde en el nivel 3, vuelve al nivel 1
					if self.nivel == 4:
						total = str((time.time()-inicial))
						self.archivarTiempos(total)
						pygame.quit()
					# Se limpia la matriz para dibujar las barras del siguiente nivel
					self.matriz = []
					# Se vuelve a crear la matriz
					self.crearMatriz()
					# Se definen las condiciones de acuerdo con cada nivel
					if self.nivel == 1:
						self.tiempo = TIEMPO_NIVEL1
						if self.modo == "Single":
							self.barra1 = Barra(1,2,TAMAÑO_BARRA_1,1) 
							self.barra2 = Barra(38,2,TAMAÑO_BARRA_1,1)
						else:
							self.barra1 = Barra_doble(1,2,9,13,TAMAÑO_BARRA_1)
							self.barra2 = Barra_doble(38,12,32,3,TAMAÑO_BARRA_1)

					elif self.nivel == 2:
						self.tiempo = TIEMPO_NIVEL2
						if self.modo == "Single":
							self.barra1 = Barra(1,2,TAMAÑO_BARRA_2,1) 
							self.barra2 = Barra(38,2,TAMAÑO_BARRA_2,1)
						else:
							self.barra1 = Barra_doble(1,2,9,13,TAMAÑO_BARRA_2)
							self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_2)

					elif self.nivel == 3:
						self.tiempo = TIEMPO_NIVEL3
						if self.modo == "Single":
							self.barra1 = Barra(1,2,TAMAÑO_BARRA_3,1) 
							self.barra2 = Barra(38,2,TAMAÑO_BARRA_3,1)
						else:
							self.barra1 = Barra_doble(1,2,9,13,TAMAÑO_BARRA_3)
							self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_3)
			else:
				if self.bola.get_score1() == 100:
					# Se reinician los scores
					self.bola.set_score1(0)
					# Se pasa de nivel
					self.nivel += 1
					self.musicSpeed +=1 
					self.playMusic()
					# Se limpia la matriz para dibujar las barras del siguiente nivel
					self.matriz = []
					# Se vuelve a crear la matriz
					self.crearMatriz()
					if self.nivel == 1:
						self.tiempo = self.time
						if self.tamaño != None:
							if self.modo == "Single":
								self.barra1 = Barra(1,2,self.tamaño,1) 
								self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA,1)
							else:
								self.barra1 = Barra_doble(1,3,9,13,self.tamaño)
								self.barra2 = Barra(38,0,TAMAÑO_BARRA_PRACTICA,1)

			# Eventos de las teclas
			pygame.init()
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
						pygame.quit()
						quit()

			# Aquí se actualiza constántemente la matriz para que
			# ocurra el movimiento de forma continua
			self.dibujarMatriz()

			self.dibujar()

			# Lee los estimulos del Arduino
			self.leerArduino()
			self.sendArduino()

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
		if self.trampolin == 1:
			if self.versus == "practica":
				if self.time == TIEMPO_NIVEL1:
					self.trampolin3.posicionar(self.matriz)
				elif self.time == TIEMPO_NIVEL2:
					self.trampolin1.posicionar(self.matriz)
					self.trampolin2.posicionar(self.matriz)
				elif self.time == TIEMPO_NIVEL3:
					self.trampolin1.posicionar(self.matriz)
					self.trampolin2.posicionar(self.matriz)
					self.trampolin3.posicionar(self.matriz)

			else:
				if self.nivel == 1:
					self.trampolin3.posicionar(self.matriz)
				elif self.nivel == 2:
					self.trampolin1.posicionar(self.matriz)
					self.trampolin2.posicionar(self.matriz)
				elif self.nivel == 3:
					self.trampolin1.posicionar(self.matriz)
					self.trampolin2.posicionar(self.matriz)
					self.trampolin3.posicionar(self.matriz)
		pygame.display.update()

	def playMusic(self):
		pygame.init()
		if self.musicSpeed == 1:
			back_music = pygame.mixer.music.load(os.path.join("sounds", "music.ogg"))
		elif self.musicSpeed == 2:
			back_music = pygame.mixer.music.load(os.path.join("sounds", "music_speed2.ogg"))
		elif self.musicSpeed == 3:
			back_music = pygame.mixer.music.load(os.path.join("sounds", "music_speed3.ogg"))
		if self.musicOn == 1:
			pygame.mixer.music.play(-1)
		else:
			pygame.mixer.music.play(-1)
			pygame.mixer.music.pause()

	# Cambia el color por uno aleatorio
	def colorCycle(self):
		self.background_color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

	# Lee las instrucciones del Arduino con Pyserial
	def leerArduino(self):
		try:
			entrada = str(ser.readline())
			datos = entrada[entrada.index("") + 1: entrada.index("\\")]
			comando = datos[:datos.index("%")]
			print(comando)
			if comando == "'P1_UP":
				self.barra1.mover(1, self.matriz)
			elif comando == "'P1_DOWN":
				self.barra1.mover(-1, self.matriz)
			elif comando == "'P2_UP":
				self.barra2.mover(1, self.matriz)
			elif comando == "'P2_DOWN":
				self.barra2.mover(-1, self.matriz)
			elif comando == "'MUTE":
				if self.musicOn == 1:
					self.musicOn = 0
					pygame.mixer.music.pause()
					self.bola.set_mute(1)
				else:
					self.musicOn = 1
					pygame.mixer.music.unpause()
					self.bola.set_mute(0)
			elif comando == "'COLOR":
				self.colorCycle()
		except:
			print('NO INPUT')
			time.sleep(0.0001)

	#def sendArduino(self):
	#	if self.bola.get_score1() == 0:
	#		ser.write(b'0')
	#	elif self.bola.get_score1() == 1:
	#		ser.write(b'1')
	#	elif self.bola.get_score1() == 2:
	#		ser.write(b'2')
	#	elif self.bola.get_score1() == 3:
	#		ser.write(b'3')
	#	elif self.bola.get_score1() == 4:
	#		ser.write(b'4')
	#	elif self.bola.get_score1() == 5:
	#		ser.write(b'5')
	#	if self.bola.get_score2() == 0:
	#		ser.write(b'6')
	#	elif self.bola.get_score2() == 1:
	#		ser.write(b'7')
	#	elif self.bola.get_score2() == 2:
	#		ser.write(b'8')
	#	elif self.bola.get_score2() == 3:
	#		ser.write(b'9')
	#	elif self.bola.get_score2() == 4:
	#		ser.write(b':')
	#	elif self.bola.get_score2() == 5:
	#		ser.write(b';')


	def archivarTiempos(self, total):  
		vent = Tk()
		vent.title("Mejores Tiempos de Juego")
		vent.minsize (800, 500)
		vent.config(bg="black")
		pygame.quit()

		def unirLista(matriz):  # Invierte las funciones de separar para la modificación del archivo txt
			if matriz == []:
				return []
			else:
				return [";".join(matriz[0])] + unirLista(matriz[1:])

		def abrirArchivo(archivo, modo): #abre el archivo
			file = open(archivo, modo)
			return file

		def separarTiempos(i):
			if i == len(highscore):
				return
			highscore[i] = highscore[i].replace("\n", "").split(";")
			separarTiempos(i + 1)
		archivo = abrirArchivo("Tiempos.txt", "r")
		highscore = archivo.readlines()
		separarTiempos(0)
		#print(highscore)
		archivo.close()


		def highscores():
			iniciales = entradaNombre.get()
			if iniciales != "":
				if len(highscore) < 3:
					registrar = open("Tiempos.txt", "a") #abre un archivo
					registrar.write(iniciales + ";" + total + "\n") #escribe en el archivo
					registrar.close()
					
				else:
					if iniciales != highscore[0][0] and total != highscore[0][1]:
						if iniciales != highscore[1][0] and total != highscore[1][1]:
							if iniciales != highscore[2][0] and total != highscore[2][1]:
								return highscores_aux(total, iniciales)
							else:
								messagebox.showerror("Error en los datos", "No es record")
						else:
							messagebox.showerror("Error en los datos", "No es record")
					else:
						messagebox.showerror("Error en los datos", "No es record")
			else:
				messagebox.showerror("Error en los datos", "Ingrese sus iniciales")


		def highscores_aux(valor, iniciales):
			if valor < highscore[2][1]:
				hacer = True
				if iniciales != "":
					if valor <= highscore[0][1] and hacer:
						highscore[2][0] = highscore[1][0]
						highscore[2][1] = highscore[1][1]
						highscore[1][0] = highscore[0][0]
						highscore[1][1] = highscore[0][1]
						highscore[0][0] = iniciales
						highscore[0][1] = valor
						hacer = False
					if valor <= highscore[1][1] and valor > highscore[0][1] and hacer:
						highscore[2][0] = highscore[1][0]
						highscore[2][1] = highscore[1][1]
						highscore[1][0] = iniciales
						highscore[1][1] = valor
						hacer = False
					if valor < highscore[2][1] and valor > highscore[1][1] and hacer:
						highscore[2][0] = iniciales
						highscore[2][1] = valor

			nuevo_texto = "\n".join(unirLista(highscore))
			archivo_highscores = abrirArchivo("Tiempos.txt", "w")
			archivo_highscores.write((str(nuevo_texto)))
			tiempo1.config(text = highscore[0][0] + "        " + str(highscore[0][1]))
			tiempo2.config(text = highscore[1][0] + "        " + str(highscore[1][1]))
			tiempo3.config(text = highscore[2][0] + "        " + str(highscore[2][1]))

		labelNombre = Label(vent, text = "¡Tiempo récord! \n Ingrese sus iniciales:", font = ("arial bold", 30), bg = "black", fg = "yellow")
		labelNombre.place (x = 200, y = 250)
		entradaNombre = Entry (vent, font = ("arial", 16), width = 25, bg = "grey")
		entradaNombre.place (x = 257, y = 380)

		if len(highscore) == 3:
			tiempo1 = Label(vent, text = highscore[0][0] + "   " +  str(highscore[0][1]), font = ("arial bold", 16), bg = "black", fg = "white")
			tiempo1.place (x = 80, y = 100)
			tiempo2 = Label(vent, text = highscore[1][0] + "   " +  str(highscore[1][1]), font = ("arial bold", 16), bg = "black", fg = "white")
			tiempo2.place (x = 80, y = 150)
			tiempo3 = Label(vent, text = highscore[2][0] + "   " +  str(highscore[2][1]), font = ("arial bold", 16), bg = "black", fg = "white")
			tiempo3.place (x = 80, y = 200)
		else:
			label = Label(vent,text = "Nuevo record!", bg = "black", fg = "white", font = ("arial bold", 16))
			label.place(x = 80, y = 100)

		boton = Button (vent, text = "Agregar",  font = ("arial", 12), width = 6, command = highscores)
		boton.place (x = 120, y = 10)

		def listo():
			vent.destroy()
			pygame.quit()
			self.ventana.deiconify()

		boton = Button (vent, text = "Volver al menú",  font = ("arial", 12), width = 6, command = listo)
		boton.place (x = 200, y = 10)
		vent.mainloop()

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
	pygame.quit()
