deudores = {}


for x in range(5):
    rut = input("Ingrese un rut : ")
    valores = int(input("Ingrese la deuda en pesos: "))
    deudores[rut] = valores


while True:
    rut = input("Ingrese el RUT del deudor (o presione Enter para terminar): ")
    if rut == "":
        break

    if rut in deudores:
        abono = int(input("Ingrese el abono: "))
        deudores[rut] -= abono

     
        if deudores[rut] <= 0:
            del deudores[rut]
    else:
        print("RUT no identificado, intente nuevamente.")

    print(deudores)

print("Los deudores finales: ")
for rut in deudores:
    print("RUT:", rut, "Deuda:", deudores[rut], "pesos")
