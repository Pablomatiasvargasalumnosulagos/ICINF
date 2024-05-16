num = int(input("Ingrese el sueldo del trabajador (o -1 para finalizar): "))
acum = 0
cont_1 = 0  
cont_2 = 0  

while num != -1:
    acum += num
    if num >= 500000 and num <= 900000:
        cont_1 += 1
    elif num > 900000 and num <= 1500000:
        cont_2 += 1
    num = int(input("Ingrese el sueldo del trabajador (o -1 para finalizar): "))

print("La cantidad de trabajadores que ganan entre $500.000 y $900.000 es:", cont_1)
print("La cantidad de trabajadores que ganan más de $900.000 es:", cont_2)
print("La empresa gasta por los sueldos un total de:", acum)
