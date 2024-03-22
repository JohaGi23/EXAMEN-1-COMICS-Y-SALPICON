print("***BIENVENIDO A TU SALPICON***")
print("***************************")

salpicon = []

def registrarFruta():
    idFruta = len(salpicon) + 1
    nombre = input("Ingrese el nombre de la fruta: ")
    precioUnitario = float(input("Ingrese el precio unitario de la fruta: "))
    cantidad = int(input("Ingrese la cantidad de esta fruta: "))

    fruta = {
        "id": idFruta,
        "nombre": nombre,
        "precio_unitario": precioUnitario,
        "cantidad": cantidad
    }

    salpicon.append(fruta)
    print("Fruta registrada con éxito.")

def mostrarCostoTotal():
    costoTotal = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in salpicon)
    print(f"El costo total del salpicón es: {costoTotal}")

def mostrarFrutasOrdenadasPorCosto():
    frutasOrdenadas = sorted(salpicon, key=lambda x: x["precio_unitario"] * x["cantidad"], reverse=True)
    print("Frutas ordenadas por costo (de mayor a menor):")
    for fruta in frutasOrdenadas:
        print(f"Nombre: {fruta['nombre']}, Costo Total: {fruta['precio_unitario'] * fruta['cantidad']}")

def mostrarFrutaMasBarata():
    frutaMasBarata = min(salpicon, key=lambda x: x["precio_unitario"])
    print(f"La fruta más barata es: {frutaMasBarata['nombre']} con precio unitario de {frutaMasBarata['precio_unitario']}")

def menu():
    while True:
        print("\n-- Menú --")
        print("1. Registrar una fruta")
        print("2. Mostrar costo total del salpicón")
        print("3. Mostrar todas las frutas ordenadas por costo")
        print("4. Mostrar la fruta más barata")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarFruta()
        elif opcion == "2":
            mostrarCostoTotal()
        elif opcion == "3":
            mostrarFrutasOrdenadasPorCosto()
        elif opcion == "4":
            mostrarFrutaMasBarata()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()

print("***GRACIAS POR TU SALPICÓN***")

