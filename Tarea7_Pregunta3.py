supermecado={}


while True:

    producto = input("Escriba el nombre del producto: ")
    if producto == "":
        break 
    cantidad = int(input("Ingrese la cantidad del producto: "))
    supermecado[producto]=cantidad


print("Productos ingresados", supermecado)


x=int(input("Ingrese el numero a multiplicar: "))

for producto, cantidad in supermecado.items():
 res = cantidad * x
 print(producto ,res)