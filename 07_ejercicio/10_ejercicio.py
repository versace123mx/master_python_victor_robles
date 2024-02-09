
contador = 1
aprobados = 0
reprobados = 0
while contador <= 15:
    calificacion = float(input(f"Ingresa calificacion alumno {contador}: "))
    if calificacion >= 6:
        aprobados +=1
    else:
        reprobados +=1
    contador+=1

print(f"Numero de alumnos aprobados {aprobados}")
print(f"Numero de alumnos reprobados {reprobados}")