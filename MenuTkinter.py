	# Pong v2.0
	# II Tarea Programada
	# Taller de Programación
	# Estudiantes: Abigail Abarca. Jessica Espinoza. Alejandro Ibarra
	# Profesor: Jeff Schmidt Peralta
	# I Semestre 2018.

from juego import *
from tkinter import *
import os
import pygame

ventana = None

IDIOMA = 0
ESP = 0
ENG = 1

def inicio():
	global ventana
	TIEMPO_NIVEL1 = 0.1
	TIEMPO_NIVEL2 = 0.07
	TIEMPO_NIVEL3 = 0.04

	# Matriz con lista de textos en ingles y español
	traduccion =[["1 Paleta IA", "1 Racket AI"], #0
	               ["2 Paletas IA", "2 Rackets AI"],#1
	               ["1 Paleta 2J", "1 Racket 2P"],#2
	               ["2 Paletas 2J", "2 Rackets 2P"],#3
	               ["Modo Práctica", "Practice Mode"], #4
	               ["Activar Trampolín", "Activate Trampoline"] #5
	               ]
	 
	# Variables globales
	IDIOMA = 0
	ESP = 0
	ENG = 1

	# Hace la ventana
	ventana = Tk ( ) 
	# Le pone el título a la ventana
	ventana.title ("Pong") 
	# Define el tamaño de la ventana
	ventana.minsize(800, 500) 
	# El tamaño no se puede modificar
	ventana.resizable (width = NO, height = NO) 
	ventana.config(bg="black")

	# Iniciar Pygame
	pygame.init()

	# Funcion para cambiar idioma de textos
	def cambiarIdioma():
	    global IDIOMA
	    IDIOMA = 1 - IDIOMA
	    oneplayer_label.config(text=traduccion[0][IDIOMA])
	    oneplayertworacket_label.config(text=traduccion[1][IDIOMA])
	    twoplayer_label.config(text=traduccion[2][IDIOMA])
	    twoplayertworacket_label.config(text=traduccion[3][IDIOMA])
	    imagen_idioma.config(image=imagenes[0][IDIOMA])
	    btn_practica.config(text = traduccion[4][IDIOMA])
	    c.config(text = traduccion[5][IDIOMA])

	# Funcion para cargar imagenes
	def loadPicture(name):
	        route = os.path.join("images", name)
	        photo = PhotoImage(file = route)
	        return photo

	# Carga de imagenes
	racket1cpuicon = loadPicture("1racketcpu.gif")
	racket12picon = loadPicture("1racket2p.gif")
	racket2cpuicon = loadPicture("2racketcpu.gif")
	racket22picon = loadPicture("2racket2p.gif")
	mainlogo = loadPicture("mainlogo.gif")
	racket2icon = loadPicture("2racket.gif")
	abouticon = loadPicture("abouticon.gif")
	cpuicon = loadPicture("cpuicon.gif")
	helpicon = loadPicture("helpicon.gif")
	backicon = loadPicture("backicon.gif")
	abigail = loadPicture("abigail.gif")
	alejandro = loadPicture("alejandro.gif")
	jessica = loadPicture("jessica.gif")
	python = loadPicture("python.gif")
	español = loadPicture("español.gif")
	ingles = loadPicture("ingles.gif")
	trampoline = loadPicture("trampoline.gif")
	galaxy = loadPicture("galaxy.gif")
	planet1 = loadPicture("planet1.gif")
	planet2 = loadPicture("planet2.gif")
	planet3 = loadPicture("planet3.gif")
	comet = loadPicture("comet.gif")

	imagenes = [[español,ingles]]
	#Opcion de jugar con una paleta contra otro humano
	def Single_humano():
		ventana.withdraw()
		juego = Juego(trampolin.get(),"Single", 1, "humano", ventana)
		juego.jugar()

	# Opcion de jugar con una paleta contra el CPU
	def Single_cpu():
		ventana.withdraw()
		juego = Juego(trampolin.get(),"Single", 1, "cpu", ventana)
		juego.jugar()

	# Opcion de jugar con dos paletas contra otro humano
	def Double_humano():
		ventana.withdraw()
		juego = Juego(trampolin.get(),"Double", 1, "humano", ventana)
		juego.jugar()

	# Opcion de jugar con dos paletas contra el CPU
	def Double_cpu():
		ventana.withdraw()
		juego = Juego(trampolin.get(),"Double", 1, "cpu", ventana)
		juego.jugar()

	# Ventana de informacion de programadores
	def about_ventana():
		ventana.withdraw()
		aboutventana = Toplevel()
		aboutventana.title("About")
		aboutventana.minsize(800, 500)
		aboutventana.resizable(width = NO, height = NO)
		
		aboutlabel = Label(aboutventana, text = "About the programmers", font = "Courier 30")
		aboutlabel.place(x = 240, y = 30)
		abigailpic = Label(aboutventana, image = abigail)
		abigailpic.place(x = 50, y = 120)
		abigailinfo = Label(aboutventana, text = "Abigail Abarca", font = "Courier 20")
		abigailinfo.place(x = 50, y = 350)
		alejandropic = Label(aboutventana, image = alejandro)
		alejandropic.place(x = 550, y = 130)
		alejandroinfo = Label(aboutventana, text = "Alejandro Ibarra", font = "Courier 20")
		alejandroinfo.place(x = 550, y = 350)
		jessicapic = Label(aboutventana, image = jessica)
		jessicapic.place(x = 280, y = 130)
		jessicainfo = Label(aboutventana, text = "Jessica Espinoza", font = "Courier 20")
		jessicainfo.place(x = 275, y = 350)
		pythonpic = Button(aboutventana, image = python)
		pythonpic.place(x = 740, y = 10)

		# Para ir atras al menu
		def back():
			aboutventana.destroy()
			ventana.deiconify()

		backbutton = Button(aboutventana, image = backicon, command = back)
		backbutton.place(x = 20, y = 20)

	# Ventana de instrucciones/ayuda
	def help_ventana():
		ventana.withdraw()
		helpventana = Toplevel()
		helpventana.title("About")
		helpventana.minsize(800, 500)
		helpventana.resizable(width = NO, height = NO)
		helpventana.config(bg = 'black')

		instructionstitle = Label(helpventana, text = "Instructions/Instrucciones", font = "Courier 28", fg = "white", bg = "black")
		instructionstitle.place(x = 240, y = 40)

		# Instrucciones, texto
		instructions = Label(helpventana, text = "P1 press W key to go up and S to go down.\
	 \nP2 UP key and DOWN key. I don't really think I have to explain \nit any further.\n \n1.\
Select the game mode\n2.If you get more than 5 points, you level up.\n3.\
There are 3 levels, every level speeds the ball up and reduces \n  the length of the paddle.", \
		 justify = LEFT, font = "Courier 18", fg = "white", bg = "black")
		instructions.place(x = 40, y = 125)
		instructionsesp = Label(helpventana, text = "J1 presiona la tecla W para subir y S para bajar.\n\
J2 tecla ARRIBA y ABAJO. No creo que tenga que explicar más. :)\n1.Selecciona el modo de juego.\
\n2.Si ganas más de 5 puntos, subes de nivel.\n3.\
Hay 3 niveles, cada nivel aumenta la velocidad de la bola y \n  reduce la longitud de la paleta.", \
	justify = LEFT, font = "Courier 18", fg = "white", bg = "black")

		instructionsesp.place(x = 40, y = 315)

		def back(): 
			helpventana.destroy()
			ventana.deiconify()

		backbutton = Button(helpventana, image = backicon, command = back)
		backbutton.place(x = 20, y = 20)


	def ventana_practica():
		ventana.withdraw()
		modo_practica = Toplevel()
		modo_practica.title("About")
		modo_practica.minsize(800, 500)
		modo_practica.resizable(width = NO, height = NO)
		modo_practica.config(bg = "black")

		def practica9_tiempo1_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=9, time=TIEMPO_NIVEL1)
			juego.jugar()	
		def practica9_tiempo1_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=9, time=TIEMPO_NIVEL1)
			juego.jugar()	

		def practica9_tiempo2_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=9, time=TIEMPO_NIVEL2)
			juego.jugar()
		def practica9_tiempo2_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=9, time=TIEMPO_NIVEL2)
			juego.jugar()	

		def practica9_tiempo3_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=9, time=TIEMPO_NIVEL3)
			juego.jugar()
		def practica9_tiempo3_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=9, time=TIEMPO_NIVEL3)
			juego.jugar()	

		def practica6_tiempo1_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=6, time=TIEMPO_NIVEL1)
			juego.jugar()
		def practica6_tiempo1_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=6, time=TIEMPO_NIVEL1)
			juego.jugar()

		def practica6_tiempo2_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=6, time=TIEMPO_NIVEL2)
			juego.jugar()
		def practica6_tiempo2_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=6, time=TIEMPO_NIVEL2)
			juego.jugar()

		def practica6_tiempo3_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=6, time=TIEMPO_NIVEL3)
			juego.jugar()
		def practica6_tiempo3_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=6, time=TIEMPO_NIVEL3)
			juego.jugar()

		def practica3_tiempo1_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=3, time=TIEMPO_NIVEL1)
			juego.jugar()
		def practica3_tiempo1_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=3, time=TIEMPO_NIVEL1)
			juego.jugar()

		def practica3_tiempo2_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=3, time=TIEMPO_NIVEL2)
			juego.jugar()
		def practica3_tiempo2_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=3, time=TIEMPO_NIVEL2)
			juego.jugar()

		def practica3_tiempo3_S():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Single", 1, "practica", ventana, tamaño=3, time=TIEMPO_NIVEL3)
			juego.jugar()
		def practica3_tiempo3_D():
			modo_practica.withdraw()
			juego = Juego(trampolin.get(),"Double", 1, "practica", ventana, tamaño=3, time=TIEMPO_NIVEL3)
			juego.jugar()

		planet1_label = Label(modo_practica, image = planet1, bg = 'black')
		planet1_label.place(x = 680, y = 20)
		planet2_label = Label(modo_practica, image = planet2, bg = 'black')
		planet2_label.place(x = 50, y = 180)
		comet_label = Label(modo_practica, image = comet, bg = 'black')
		comet_label.place(x = 500, y = 150)

		label9 = Label(modo_practica, text="9", font = "Courier 45", fg = "white", bg = "black")
		label9.place(x=80, y=90)
		label6 = Label(modo_practica, text="6", font = "Courier 45", fg = "white", bg = "black")
		label6.place(x=80, y=190)
		label3 = Label(modo_practica, text="3", font = "Courier 45", fg = "white", bg = "black")
		label3.place(x=80, y=290)

		label9_Single = Label(modo_practica, text="Single", font = "Courier 18", fg = "white", bg = "black")
		label9_Single.place(x=280, y=100)
		label6_Single = Label(modo_practica, text="Single", font = "Courier 18", fg = "white", bg = "black")
		label6_Single.place(x=280, y=200)
		label3_Single = Label(modo_practica, text="Single", font = "Courier 18", fg = "white", bg = "black")
		label3_Single.place(x=280, y=300)	
		label9_Double = Label(modo_practica, text="Double", font = "Courier 18", fg = "white", bg = "black")
		label9_Double.place(x=280, y=130)
		label6_Double = Label(modo_practica, text="Double", font = "Courier 18", fg = "white", bg = "black")
		label6_Double.place(x=280, y=230)
		label3_Double = Label(modo_practica, text="Double", font = "Courier 18", fg = "white", bg = "black")
		label3_Double.place(x=280, y=330)

		btn9_timepo1_S = Button(modo_practica, text= "Level 1", command = practica9_tiempo1_S)
		btn9_timepo1_S.place(x = 400, y = 100)
		btn9_timepo1_D = Button(modo_practica, text= "Level 1", command = practica9_tiempo1_D)
		btn9_timepo1_D.place(x = 400, y = 130)
		btn9_timepo2_S = Button(modo_practica, text= "Level 2", command = practica9_tiempo2_S)
		btn9_timepo2_S.place(x = 500, y = 100)
		btn9_timepo2_D = Button(modo_practica, text= "Level 2", command = practica9_tiempo2_D)
		btn9_timepo2_D.place(x = 500, y = 130)
		btn9_timepo3_S = Button(modo_practica, text= "Level 3", command = practica9_tiempo3_S)
		btn9_timepo3_S.place(x = 600, y = 100)
		btn9_timepo3_D = Button(modo_practica, text= "Level 3", command = practica9_tiempo3_D)
		btn9_timepo3_D.place(x = 600, y = 130)
		btn6_timepo1_S = Button(modo_practica, text= "Level 1", command = practica6_tiempo1_S)
		btn6_timepo1_S.place(x = 400, y = 200)
		btn6_timepo1_D = Button(modo_practica, text= "Level 1", command = practica6_tiempo1_D)
		btn6_timepo1_D.place(x = 400, y = 230)
		btn6_timepo2_S = Button(modo_practica, text= "Level 2", command = practica6_tiempo2_S)
		btn6_timepo2_S.place(x = 500, y = 200)
		btn6_timepo2_D = Button(modo_practica, text= "Level 2", command = practica6_tiempo2_D)
		btn6_timepo2_D.place(x = 500, y = 230)
		btn6_timepo3_S = Button(modo_practica, text= "Level 3", command = practica6_tiempo3_S)
		btn6_timepo3_S.place(x = 600, y = 200)
		btn6_timepo3_D = Button(modo_practica, text= "Level 3", command = practica6_tiempo3_D)
		btn6_timepo3_D.place(x = 600, y = 230)
		btn3_timepo1_S = Button(modo_practica, text= "Level 1", command = practica3_tiempo1_S)
		btn3_timepo1_S.place(x = 400, y = 300)
		btn3_timepo1_D = Button(modo_practica, text= "Level 1", command = practica3_tiempo1_D)
		btn3_timepo1_D.place(x = 400, y = 330)
		btn3_timepo2_S = Button(modo_practica, text= "Level 2", command = practica3_tiempo2_S)
		btn3_timepo2_S.place(x = 500, y = 300)
		btn3_timepo2_D = Button(modo_practica, text= "Level 2", command = practica3_tiempo2_D)
		btn3_timepo2_D.place(x = 500, y = 330)
		btn3_timepo3_S = Button(modo_practica, text= "Level 3", command = practica3_tiempo3_S)
		btn3_timepo3_S.place(x = 600, y = 300)
		btn3_timepo3_D = Button(modo_practica, text= "Level 3", command = practica3_tiempo3_D)
		btn3_timepo3_D.place(x = 600, y = 330)

		def back():
			modo_practica.destroy()
			ventana.deiconify()

		backbutton = Button(modo_practica, image = backicon, command = back)
		backbutton.place(x = 20, y = 20)
		# Para ir atras en el menu


	# Textos e imagenes de menu
	galaxy_label = Label(ventana, image = galaxy, bg = 'black')
	galaxy_label.place(x = 105, y = 130)
	mainlogo_label = Label(ventana, image = mainlogo, bg = 'black')
	mainlogo_label.place(x = 220, y = 20)
	oneplayer_label = Label(ventana, text=traduccion[0][IDIOMA], font = "Courier 20", fg = "white", bg = "black")
	oneplayer_label.place(x = 110, y = 270)
	oneplayertworacket_label = Label(ventana, text=traduccion[1][IDIOMA], font = "Courier 20", fg = "white", bg = "black")
	oneplayertworacket_label.place(x = 500, y = 270)
	twoplayer_label = Label(ventana, text=traduccion[2][IDIOMA], font = "Courier 20", fg = "white", bg = "black")
	twoplayer_label.place(x = 125, y = 405)
	twoplayertworacket_label = Label(ventana, text=traduccion[3][IDIOMA], font = "Courier 20", fg = "white", bg = "black")
	twoplayertworacket_label.place(x = 500, y = 405)

	trampolin = IntVar()

	# Botones de inicio de juego
	oneplayer_button = Button(ventana, image = racket1cpuicon, command = Single_cpu)
	oneplayer_button.place(x = 100, y = 180)
	twoplayer_button = Button(ventana, image = racket12picon, command = Single_humano)
	twoplayer_button.place(x = 100, y = 315)
	oneplayer2r_button = Button(ventana, image = racket2cpuicon, command = Double_cpu)
	oneplayer2r_button.place(x = 450, y = 180)
	twoplayer2r_button = Button(ventana, image = racket22picon, command = Double_humano)
	twoplayer2r_button.place(x = 450, y = 315)
	about_button = Button(ventana, image = abouticon, command = about_ventana)
	about_button.place(x = 25, y = 40)
	help_button = Button(ventana, image = helpicon, command = help_ventana, bg = "black")
	help_button.place(x = 100, y = 40)
	imagen_idioma = Button(ventana, image=imagenes[0][IDIOMA], font = "Courier 16", command = cambiarIdioma)
	imagen_idioma.place(x = 700, y = 40)
	btn_practica = Button(ventana, text=traduccion[4][IDIOMA], command = ventana_practica)
	btn_practica.place(x=250, y=455)
	c = Checkbutton(ventana, text = traduccion[5][IDIOMA],variable = trampolin,onvalue = 1, offvalue = 0)
	c.place(x = 400, y = 455)
	mainloop()

inicio()
