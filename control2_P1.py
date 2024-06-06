

lista=[]
for x in range(1,16):
    num=int(input("Ingrese el puntaje obtenido por el alumno: "))
    lista.append(num)

    print(lista)

if num >= 60: 
    for dia in range (1,16):
     print("Los dias", dia, "el alumno obtuvo un puntaje mayor o igual a 60 puntos")

else:
     if num < 60:
         for dia in range (1,16):
           print("Los dias", dia, "el alumno obtuvo un puntaje menor a 60 puntos" )        
    
