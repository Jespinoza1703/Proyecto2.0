# Clase Barra:
# Atributos:
# ancho
# largo
# x1
# y1
# x2
# y2
####################### 
# Metodos:
# posicionar()
# get_x1()
# get_y()
# get_x2()
# get_y2
# mover()

#Objeto barra doble
class Barra_doble:
	def __init__(self,x1,y1,x2,y2,largo):
		self.ancho = 1
		self.largo = largo
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	# Coloca la barra en la matriz
	def posicionar(self,matriz):
		for n in range(self.largo):
			matriz[self.y1+n][self.x1] = 1
		for n in range(self.largo):
			matriz[self.y2+n][self.x2] = 1
	# Funciones get() para obtener valores 
	def get_x1(self):
		return self.x1

	def get_y(self):
		return self.y1

	def get_x2(self):
		return self.x2

	def get_y2(self):
		return self.y2

	# Permite mover la barra sin que mueva a través de la matriz
	def mover(self,vy,matriz):
		# Se dan restricciones para que la barra no se salga de la pantalla
		if vy == -1 and self.y1 + self.largo < 25 and self.y2 + self.largo < 25:
			# La posicion anterior (de donde se mueve) se pinta de negro
			matriz[self.y1][self.x1] = 0
			matriz[self.y2][self.x2] = 0
			# Se mueve de una en una posicion
			self.y1 -= vy
			self.y2 -= vy
			# La nueva pocision se pinta de negro
			matriz[self.y1][self.x1] = 1
			matriz[self.y2][self.x2] = 1
		elif vy == 1 and self.y1 > 0 and self.y2 > 0:
			matriz[self.y1 + self.largo - 1][self.x1] = 0
			matriz[self.y2 + self.largo - 1][self.x2] = 0
			self.y1 -= vy
			self.y2 -= vy
			matriz[self.y1][self.x1] = 1
			matriz[self.y2][self.x2] = 1
