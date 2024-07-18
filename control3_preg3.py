
def potencia(num,exp):
   res=1
   cont=0
   while cont < exp:
      res = res*num
      cont=cont + 1
   return res   


num= int(input("Ingrese la base: "))
exp=int(input("Ingrese el exponente: "))
print(potencia(num,exp))

