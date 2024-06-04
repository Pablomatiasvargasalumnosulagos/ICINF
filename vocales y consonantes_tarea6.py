def contar_vocales_consonantes(word):
    vocales= "aeiouAEIOU"
    num_vocales = sum(1 for letra in word if letra in vocales  )
    num_consonantes = sum(1 for letra in word if letra.isalpha()and letra not in vocales )
    return num_vocales, num_consonantes

words = []

while True:
    word = input("Ingrese una palabra, o presione Enter para finalizar:  ") 
    if word == "":
        break
    words.append(word)

for word in words:
    vocales, consonantes = contar_vocales_consonantes(word)
    
    print("La palabra '" + word + "' tiene " + str(vocales) + " vocales y " + str(consonantes) + " consonantes.")