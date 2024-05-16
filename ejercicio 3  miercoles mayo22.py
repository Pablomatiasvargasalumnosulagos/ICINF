
a = float(input("Ingrese una altura: "))  
acum=0
cont=0
while a != 0:
  acum = acum+a
  cont = cont + 1
  a=float(input("Ingrese una altura: "))     
promedio = acum / cont

print("El promedio es : ",  promedio, "metros"  )
