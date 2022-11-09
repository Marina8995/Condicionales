#EJEMPLO BECA: 
# Si tiene un salario inferior tiene derecho a beca (aunque no se cumplan las otras dos condiciones). 
# Si no se cumple la condición de salario pero sí las otras dos también tiene derecho a beca.

print("Programa de becas año 2022")
distancia_escuela=int(input("Introduce la distancia a la escuela "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el nº de hermanos en el centro "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")