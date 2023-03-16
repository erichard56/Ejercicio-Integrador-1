from abc import ABC

#ejercicio 7
class Persona(ABC):
	def __init__(self, nombre, edad = 0, dni = 0):
		self.__nombre = nombre
		self.__edad = edad
		self.__dni = dni
    
	@property
	def nombre(self):
		return(self.__nombre)
	
	@nombre.setter
	def nombre(self, nuevo_nombre):
		if (len(nuevo_nombre) > 0):
			self.__nombre = nuevo_nombre
		else:
			print('el nombre debe ser distinto de null')
	
	@property
	def edad(self):
		return(self.__edad)
	
	@edad.setter
	def edad(self, nueva_edad):
		if (type(nueva_edad) == int):
			if (nueva_edad >= 0):
				self.__edad = nueva_edad
				return(True)
			else:
				print('edad debe ser mayor o igual a 0')
				return (False)
		else:
			print('edad debe ser un dato numérico')
			return (False)
	
	@property
	def dni(self):
		return(self.__dni)
	
	@dni.setter
	def dni(self, nuevo_dni):
		if (type(nuevo_dni) == int):
			if (nuevo_dni > 0):
				self.__dni = nuevo_dni
				return(True)
			else:
				print('dni debe ser mayor a 0')
				return(False)
		else:
			print('dni debe ser un dato numérico')
			return(False)

	def mostrar(self):
		return(f"Nombre {self.nombre}, edad {self.edad}, dni {self.dni}")
	
	def es_mayor_de_edad(self):
		return(self.__edad > 18)

class Cuenta(Persona):
	def __init__(self, titular, edad = 0, dni = 0, cantidad = 0):
		super().__init__(titular, edad, dni)
		self.__cantidad = cantidad

	def __str__(self):
		return(f'{self.__nombre}, {self.__edad}, {self.__dni}, {self.__cantidad}')

	@property
	def cantidad(self):
		return(self.__cantidad)

	@cantidad.setter
	def cantidad(self, nueva_cantidad):
		if (type(nueva_cantidad) == int or type(nueva_cantidad) == float):
			self.__cantidad = nueva_cantidad
		else:
			print('cantidad debe ser int o float')

	def mostrar(self):
		return(f'Titular {self.nombre}, cantidad {self.__cantidad}')
	
	def ingresar(self, nueva_cantidad):
		if (type(nueva_cantidad) == int or type(nueva_cantidad) == float):
			if (nueva_cantidad > 0):
				self.__cantidad += nueva_cantidad
			else:
				print('cantidad debe ser un número positivo')
		else:
			print('Cantidad debe ser int o float')

	def retirar(self, nueva_cantidad):
		if (type(nueva_cantidad) == int or type(nueva_cantidad) == float):
			self.__cantidad -= nueva_cantidad
		else:
			print('Cantidad a retirar debe ser int o float')

class CuentaJoven(Cuenta):
	def __init__(self, titular, edad, dni, cantidad, bonificacion):
		super().__init__(titular, edad, dni, cantidad)
		self.__bonificacion = bonificacion

	def __str__(self):
		return(f'{self.__nombre} {self.__cantidad} {self.__bonificacion}')
	
	@property
	def bonificacion(self):
		return(self.__bonificacion)
	
	@bonificacion.setter
	def bonificacion(self, nueva_bonificacion):
		if (type(nueva_bonificacion) == int or type(nueva_bonificacion) == float):
			self.__bonificacion = nueva_bonificacion
		else:
			print('bonificacion deber set int o float')

	def es_titular_valido(self):
		return(self.es_mayor_de_edad() and self.edad <= 25)

	def retirar(self, nueva_cantidad):
		if (self.es_titular_valido()):
			if (type(nueva_cantidad) == int or type(nueva_cantidad) == float):
				self.cantidad -= nueva_cantidad
			else:
				print('cantidad debe ser int o float')
		else:
			print('titular invalido')

	def mostrar(self):
		return (f'Cuenta Joven, Bonificacion {self.__bonificacion}')

