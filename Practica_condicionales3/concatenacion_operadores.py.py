edad=7
if 0>edad<100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")    

#Ejemplo salario
salario_presidente=int(input("Introduce salario presidente "))
print("Salario presidente: " +str(salario_presidente))

salario_director=int(input("Introduce salario director "))
print("Salario presidente: " +str(salario_director))

salario_jefe_area=int(input("Introduce salario jefe area "))
print("Salario presidente: " +str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario administrativo "))
print("Salario presidente: " +str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo está fallando")    