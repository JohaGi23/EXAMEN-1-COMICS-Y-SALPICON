import random

print("***BIENVENIDOS A TIENDA COMICS***")
print("*********************************")

inventario = []

def registrarProducto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario del producto: "))
    ubicacion = input("Ingrese la ubicación en la tienda (A, B, C o D): ")

    
    CantidadProductosUbicacion = sum(1 for producto in inventario if producto["ubicacion"] == ubicacion)

    print(f"Cantidad de productos en ubicación {ubicacion}: {CantidadProductosUbicacion}")

    if CantidadProductosUbicacion == 50:
        print("Error: La ubicación ya tiene 50 productos registrados.")
        return
    

    descripcion = input("Ingrese la descripción del producto: ")
    casa = input("Ingrese la casa a la que pertenece el producto (Marvel, DC, Image, etc): ")
    referencia = input("Ingrese la referencia del producto: ")
    pais = input("Ingrese el país de origen del producto: ")
    unidades = int(input("Ingrese el número de unidades existentes del producto: "))
    garantia = input("¿El producto tiene garantía extendida? (true/false): ")

    
    producto = {
        'id': random.randint(1, 100),
        "nombre": nombre,
        "precio": precio,
        "ubicacion": ubicacion,
        "descripcion": descripcion,
        "casa": casa,
        "referencia": referencia,
        "pais": pais,
        "unidades": unidades,
        "garantia": garantia== "true"
       
    }

    inventario.append(producto)
    print("Producto registrado con éxito.")


    def restarProductoUbicacion(ubicacion):
     for producto in inventario:
        if producto['ubicacion'] == ubicacion:
            producto['unidades'] -= 1
            break


def mostrarProductos():
    if inventario:
        print("Productos en bodega:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Descripción: {producto['descripcion']},Ubicacion:{producto['ubicacion']}")
    else:
        print("No hay productos en bodega.")

def buscarProductoxNombre():
    buscarNombre = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in inventario:
        if producto["nombre"] == buscarNombre:
            encontrado = True
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Descripción: {producto['descripcion']}")
    if not encontrado:
        print("No se encontró el producto en el inventario.")

def modificarUnidades():
    buscarNombre= input("Ingrese el nombre del producto que desea modificar: ")
    encontrado = False
    for producto in inventario:
        if producto['nombre'] == buscarNombre:
            encontrado = True
            nuevasUnidades = int(input(f"Ingrese el nuevo número de unidades compradas para {producto['nombre']}: "))
            if nuevasUnidades<= producto['unidades']:
                producto['unidades'] = nuevasUnidades
                print("Número de unidades compradas actualizado con éxito.")
            else:
                print("Error: El nuevo número de unidades compradas no puede ser mayor al número inicial.")
    if not encontrado:
        print("No se encontró el producto en el inventario.")

def eliminarProducto():
    buscarNombre = input("Ingrese el nombre del producto que desea eliminar: ")
    confirmacion = input(f"¿Está seguro que desea eliminar {buscarNombre}? (si/no): ")
    if confirmacion == "si":
        global inventario
        encontrado = False
        for producto in inventario[:]:  
            if producto['nombre'] == buscarNombre:
                inventario.remove(producto)
                print("Producto eliminado del inventario.")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró el producto en el inventario.")

def menu():
    while True:
        print("\n-- Menú --")
        print("1. Registrar un producto")
        print("2. Mostrar todos los productos en bodega")
        print("3. Buscar producto por nombre")
        print("4. Modificar número de unidades compradas")
        print("5. Eliminar un producto del inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarProducto()
        elif opcion == "2":
            mostrarProductos()
        elif opcion == "3":
            buscarProductoxNombre()
        elif opcion == "4":
            modificarUnidades()
        elif opcion == "5":
            eliminarProducto()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()

print("***GRACIAS POR TU COMPRA***")
