from os import system, name
from tabulate import tabulate
import json

    
def cargar_compra(stock):
    while True:
        limpiar_pantalla()
        opciones = [
            {"id": "1", "descripcion": "Buscar Producto (muestra id, precio y stock)", "accion": buscar_producto},
            {"id": "2", "descripcion": "Cantidad a Comprar", "accion": cantidad_comprar},
            {"id": "3", "descripcion": "Total a Pagar", "accion": ver_descuento},
            {"id": "4", "descripcion": "Finalizar Compra", "accion": salir},
            {"id": "5", "descripcion": "Volver al menú principal", "accion": main}
        ]

        print(tabulate(
            [[opcion["id"], opcion["descripcion"]] for opcion in opciones],
            headers=["Opción", "Descripción"],
            tablefmt="fancy_grid",
            colalign=("center", "left"),
        ))

        usuario = input("Ingrese una opción: ").strip()
        for opcion in opciones:
            if usuario == opcion["id"]:
                if opcion["id"] == "1":  # Pasar 'stock' solo para la opción 1
                    opcion["accion"](stock)
                else:
                    opcion["accion"]()  # Llamar a las otras acciones sin argumentos
                break
        else:
            print("Opción inválida, intente de nuevo.")
        

def buscar_producto(stock):
    limpiar_pantalla()
    try:
        producto_id = int(input("Ingrese el ID del producto a buscar: ").strip())
        producto = stock.get(producto_id)
        if producto:
            print("\nProducto encontrado:")
            print(tabulate(
                [[producto_id, producto["descripcion"], producto["precio"], producto["stock"]]],
                headers=["ID", "Descripción", "Precio", "Stock"],
                tablefmt="fancy_grid",
            ))
        else:
            print(f"\nEl producto con ID '{producto_id}' no existe en el stock.")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")
    input("\nPresione Enter para continuar...")


def cantidad_comprar(stock):
    pass


def ver_compras():
    while True:
        limpiar_pantalla()
        opciones = [
            {"id": "1", "descripcion": "Filtrar Compra por fecha", "accion": buscar_producto},
            {"id": "2", "descripcion": "Mostrar Ultima compra realizada","accion": cantidad_comprar},
            {"id": "3", "descripcion": "Volver al Menu Principal", "accion": main}, 
        ]

        print(tabulate(
            [[opcion["id"], opcion["descripcion"]] for opcion in opciones],
            headers=["Opción", "Descripción"],
            tablefmt="fancy_grid",
            colalign=("center", "left"),
        ))

        usuario = input("Ingrese una opción: ").strip()
        for opcion in opciones:
            if usuario == opcion["id"]:
                if opcion["id"] == "1":  # Pasar 'stock' solo para la opción 1
                    opcion["accion"](stock)
                else:
                    opcion["accion"]()  # Llamar a las otras acciones sin argumentos
                break
        else:
            print("Opción inválida, intente de nuevo.")

def ver_descuento():
    # Implementar la función ver_descuento
    pass

def generar_ticket():
    # Implementar la función generar_ticket
    pass

def agregar_productos():
    # Implementar la función agregar_productos
    pass

def cargar_productos_desde_csv(archivo_csv):
    global productos
    try:
        with open(archivo_csv, "rt", encoding="utf-8-sig") as archivo:
            productos = [linea.rstrip().split(";") for linea in archivo]
        return True  # Indica que la carga fue exitosa
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_csv}'. Verifique la ruta y vuelva a intentarlo.")
        return False
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo '{archivo_csv}': {e}")
        return False

def cargar_stock_desde_json(archivo_json):
    try:
        with open(archivo_json) as f:
            lista_stock = json.load(f)
            return {producto["id_productos"]: producto for producto in lista_stock}   # Devuelve el contenido del archivo si se cargó correctamente
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_json}'. Verifique la ruta y vuelva a intentarlo.")
        return {}
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo '{archivo_json}': {e}")
        return {}

def limpiar_pantalla():
    system("cls" if name == "nt" else "clear")

def salir():
    print("Saliendo...")
    exit()

def mostrar_opciones():
    limpiar_pantalla()
    opciones = [
        {"id": "1", "descripcion": "Cargar Compra", "accion": cargar_compra},
        {"id": "2", "descripcion": "Ver compras", "accion": ver_compras},
        {"id": "3", "descripcion": "Ver descuento del Día", "accion": ver_descuento},
        {"id": "4", "descripcion": "Generar ticket de compra", "accion": generar_ticket},
        {"id": "5", "descripcion": "Agregar productos", "accion": agregar_productos},
        {"id": "6", "descripcion": "Salir", "accion": salir}
    ]

    print(
        tabulate(
            [[opcion["id"], opcion["descripcion"]] for opcion in opciones],
            headers=["Opción", "Descripción"],
            tablefmt="fancy_grid",
            colalign=("center", "left"),
        )
    )
    
    return opciones

# Función principal del programa
def main():
    # Cargar los productos desde el archivo CSV y el stock desde JSON
    archivo_csv = "archivos/csv/productos_50.csv"
    archivo_json = "archivos/json/json_productos_stock.json"

    # Verificar si los archivos se cargan correctamente
    if not cargar_productos_desde_csv(archivo_csv):
        print("Error crítico: No se pudieron cargar los productos del archivo CSV. El programa no se ejecutará.")
        return

    stock = cargar_stock_desde_json(archivo_json)
    if stock is None:
        print("Error crítico: No se pudo cargar el stock del archivo JSON. El programa no se ejecutará.")
        return

    while True:
        opciones = mostrar_opciones()
        usuario = input("Ingrese una opción: ")

        for opcion in opciones:
            if usuario == opcion["id"]:
                if opcion["id"] == "1":
                    opcion["accion"](stock)  # Pasar stock solo para la opción 1
                else:
                    opcion["accion"]()  # Llamar a las otras acciones sin argumentos
                break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
