

print("Asignaturas optativas")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
asignatura=input("Escribe la asignatura escogida: ")
#Aqui no ponemos int porque es texto

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura elegida no está contemplada")    

#lower = para pasar todo a minúsculas
#upper

option=input("Escribe la asignatura escogida: ")
asignatura=option.lower()
