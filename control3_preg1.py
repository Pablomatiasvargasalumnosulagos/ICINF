def digitos(num):
    if num <= 9:
        print("El numero", num, "tiene 1 digito")
    elif num >= 10 and num <= 99:
        print("El numero", num, "tiene 2 digitos")
    elif num >= 100 and num <= 999:
        print("El numero", num, "tiene 3 digitos")
    elif num >= 1000 and num <= 9999:
        print("El numero", num, "tiene 4 digitos")
    elif num >= 10000:
        print("El numero", num, "tiene 5 digitos o mas")

num = int(input("Ingrese un numero: "))
digitos(num)

