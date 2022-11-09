#Ejemplo elif

print("Verificación de acceso")
edad_usuario=int(input("Introduzca su edad"))

if edad_usuario<18:
	print("No puedes pasar")
elif edad_usuario>100:
	print("Edad errónea")
else:
	print("Puedes pasar")	