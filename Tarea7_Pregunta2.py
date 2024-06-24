caracter=[]
while True:
    word=input("Escriba una palabra: ")
    if word == "":
        break
    caracter.append(word)

for word in caracter:
 
 cont_a = word.count("a") + word.count("A")


 print("La palabra '" + word + "' tiene " + str(cont_a) + " letras 'a' o 'A'")
 