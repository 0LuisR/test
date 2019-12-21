sueldo=int(input("Introduce el sueldo: "))
if sueldo>3000:
	print("El suario debe pagar impuestos")
if sueldo<=3000:
	print("El usuario no declara renta")

if sueldo>6000 and sueldo<10000:
	print("El usuario tiene que pagar una bonificación de 1000 pesos")

if sueldo==20000 or sueldo==30000:
	print("El usuario paga impuestos")