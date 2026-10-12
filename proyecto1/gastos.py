from datetime import datetime 

gastos = [] # Este array alamacena el diccionario gasto


#Programo dos funciones sencillas sin parametros
def registrar_gasto():

	cantidad = int(input("Ingresa la cantidad de dinero del gasto $: ")) # Pido las cantidad de gasto al usuario
	categoria = input("Ingresa la categoria por ejemplo, entretenimeinto, comida, transporte: ").upper() # Pido al usuario que que ingrese la categoria, y formateo el texto a mayusculas
	fecha=datetime.now() # esta variable me permite obtener la fecha actual en tiempo de registro (ejecucion del programa) para despues guardarla en el diccionario

	gasto = {} # Creeo un diccionario vacio

	gasto["cantidad"] = cantidad        # agrego el resultado de la variable en el diccionario
	gasto["categoria"] = categoria		# agrego el resultado de la variable en el diccionario
	gasto["fecha"] = fecha.strftime("%Y-%m-%d %H:%M:%S") #la fecha guardada en un formato mas completo, pero se puede un formato mas simple, y la agrego al diccionario
	gastos.append(gasto)				# agrego el diccionario al array gastos difinido al principio

	print("Gasto registrado correctamente !")

def mostrar_gastos():
# esta parte funciona: basicamente recorre para cada gasto en la lista gastos y lo imprime
	for gasto in gastos:
		print(gasto)

# pero podria ser tambien de esta forma mas clara la impresion por pantalla 
	'''for gasto in gastos:
		print(gasto["cantidad"])
		print(gasto["categoria"])'''


# Esta funcion tengo la idea de que cacule todo el dienro gastado
def calcularTotalGastos():
	pass


#Nota: Siempre es recomendable que los menus se definan al final, por que el codigo se ejecuta de arriba a bajo 
#DEFINO EL MENU
opcion = 0
while opcion != 3:
	print("\n Bienvenido a su gestor de gastos basico, por ahora")
	print("1. Registar Gasto")
	print("2. Ver Gastos")
	print("3. Salir")

	try:

		opcion = int(input("Ingresa un opcion: "))

		if opcion == 1:
			registrar_gasto()
		elif opcion == 2:
			mostrar_gastos()
		elif opcion == 3:
			print("Saliendo del programa")
			break
		else:
			print("Opcion no valida. inetenta de nuevo, elige un numero entre 1 y 3")
	except ValueError:
		print("Error: Ingresa un numero valido")