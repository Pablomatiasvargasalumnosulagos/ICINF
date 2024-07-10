def sumatoria(numero):
   if numero == 0:
      return 0
   else:
      return numero + sumatoria(numero - 1)
   
res = sumatoria(5)
print(res)   

