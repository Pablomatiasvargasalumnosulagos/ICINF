def es_binario(var):
    for char in var:
        if char != '0' and char != '1':
            return False
    return True

var = input("Ingrese una palabra: ")
print(es_binario(var))
