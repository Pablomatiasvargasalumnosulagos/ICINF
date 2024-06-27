lista=[]
for x in range(10):
   precio=int(input("Ingrese el precio en pesos chilenos:  $")) 
   lista.append(precio)
   print(lista)   
   Valor_dolar = (950/precio)
   lista[x] = Valor_dolar  
   print("Precios de CLP a dolar", lista)
