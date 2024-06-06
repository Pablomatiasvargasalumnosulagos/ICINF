lista=[]
pos=-1
largo = len(nuevo)
for x in range(1,8):
    nuevo=input("Ingrese el dato nuevo para la lista: ")
    lista.append(nuevo)
    if nuevo[pos] != nuevo[largo-pos-1]:
       es_palindromo = False
    break
    if pos >= largo / 2:
        break
    pos = pos + 1

    print(lista)


