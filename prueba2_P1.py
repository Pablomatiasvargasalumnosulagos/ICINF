notas=[]
cont = 0
cont_1 = 0
cont_2 = 0
acum = 0
while True:
    x = float(input("Ingrese una nota: "))
    acum = acum + x
    if x == 0:
     break
    cont = cont + 1
    prom = acum / cont

    if x < 4.0:
     cont_1 = cont_1 + 1
    else:
     if x >= 4.0:
      cont_2 = cont_2 + 1

     
print("La cantidad de notas ingresadas son: ",  cont)
print("El promedio de las notas es: ",  prom)
print("La cantidad de notas inferiores a 4.0 son: ",  cont_1)
print("La cantidad de notas igual o superiores a 4.0 son: ",  cont_2)