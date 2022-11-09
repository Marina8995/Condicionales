#>mayor que
#<menor que
#==igual que
#>=
#<=
#!=

#Ejemplo 1


def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(5))


#Ejemplo con consola



print("Programa de evaluación de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion
	
#int para indicar que nota_alumno es un número, si no da error	
print(evaluacion(int(nota_alumno)))

