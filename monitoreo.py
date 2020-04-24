import os
import subprocess
import time

class Monitoreo():
	monitoreo=True
	monitoreoo=True
	print("Presiona m para ver el estado de memoria")
	print("Presiona d para ver el estado del disco duro")
	print("Presiona c para ver el estado del CPU")
	print("Presiona l para ver el estado del CPU en grafica")

	time.sleep(7)
	while (monitoreo):
		try:
			subprocess.call(['nmon'])
		except:
			print("Error al iniciar nmon asegurece de tenerlo instalado")
			print("Intenta con apt-get install nmon")
		print("¿Quieres salir de nmon? y/n")	
		salir = input("Teclea y/n: ")
		while (monitoreoo):
			if salir == 'y':
				monitoreo = False
				break
			if salir == 'n':
				break
			else:
				print("Error en el caracter")
				print("¿Quieres salir de nmon? y/n")	
				salir = input("Teclea y/n: ")

				

