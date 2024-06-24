lista=[]
for x in range (10):
    numero = int(input("Ingrese un numero para la lista: "))
    lista.append(numero)

print("Lista original ingresada:", lista)


print("Lista en orden inverso : ")
for numero in reversed(lista):
    print(numero, end = " ")

print()    
    



  
