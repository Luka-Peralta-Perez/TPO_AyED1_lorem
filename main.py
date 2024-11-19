from os import system, name
from tabulate import tabulate
import json
from typing import Dict, Any

# Limpiar pantalla
def limpiar_pantalla() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Limpia la pantalla del terminal.
    """
    system("cls" if name == "nt" else "clear")


# Función para cargar compra
def cargar_compra(stock: Dict[int, Dict[str, Any]]) -> None:
    """
    Pre: `stock` debe ser un diccionario con los productos disponibles para la compra.
    Post: Muestra un menú para realizar compras, incluyendo la búsqueda de productos, cantidad a comprar y total a pagar.
    """
    while True:
        limpiar_pantalla()
        opciones = [
            {"id": "1", "descripcion": "Buscar Producto (muestra id, precio y stock)", "accion": buscar_producto},
            {"id": "2", "descripcion": "Cantidad a Comprar", "accion": cantidad_comprar},
            {"id": "3", "descripcion": "Total a Pagar", "accion": ver_descuento},
            {"id": "4", "descripcion": "Finalizar Compra", "accion": salir},
            {"id": "5", "descripcion": "Volver al menú principal", "accion": main}
        ]

        # Mostrar opciones con tabulate
        print(tabulate(
            [[opcion["id"], opcion["descripcion"]] for opcion in opciones],
            headers=["Opción", "Descripción"],
            tablefmt="fancy_grid",
            colalign=("center", "left"),
        ))

        # Selección de opción
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


# Función para buscar un producto en stock
def buscar_producto(stock: Dict[int, Dict[str, Any]]) -> None:
    """
    Pre: `stock` debe ser un diccionario con productos.
    Post: Muestra los detalles de un producto si se encuentra en el stock.
    """
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


# Función para manejar la cantidad de compra (pendiente de implementar)
def cantidad_comprar(stock: Dict[int, Dict[str, Any]]) -> None:
    """
    Pre: `stock` debe ser un diccionario con los productos disponibles para la compra.
    Post: Esta función está pendiente de implementación.
    """
    pass


# Función para mostrar compras (pendiente de implementar)
def ver_compras() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Muestra un menú para gestionar las compras.
    """
    while True:
        limpiar_pantalla()
        opciones = [
            {"id": "1", "descripcion": "Filtrar Compra por fecha", "accion": buscar_producto},
            {"id": "2", "descripcion": "Mostrar Ultima compra realizada", "accion": cantidad_comprar},
            {"id": "3", "descripcion": "Volver al Menu Principal", "accion": main},
        ]

        # Mostrar opciones con tabulate
        print(tabulate(
            [[opcion["id"], opcion["descripcion"]] for opcion in opciones],
            headers=["Opción", "Descripción"],
            tablefmt="fancy_grid",
            colalign=("center", "left"),
        ))

        # Selección de opción
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


# Funciones no implementadas
def ver_descuento() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Esta función está pendiente de implementación.
    """
    pass


def generar_ticket() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Esta función está pendiente de implementación.
    """
    pass


def agregar_productos() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Esta función está pendiente de implementación.
    """
    pass

def cierre_caja():
    pass

# Cargar productos desde CSV
def cargar_productos_desde_csv(archivo_csv: str) -> bool:
    """
    Pre: El archivo CSV debe existir en la ruta especificada y estar bien formado.
    Post: Devuelve True si el archivo se carga correctamente, False en caso contrario.
    """
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


# Cargar stock desde JSON
def cargar_stock_desde_json(archivo_json: str) -> Dict[int, Dict[str, Any]]:
    """
    Pre: El archivo JSON debe existir y tener un formato válido.
    Post: Devuelve un diccionario de stock donde las claves son los IDs de los productos.
    """
    try:
        with open(archivo_json) as f:
            lista_stock = json.load(f)
            return {producto["id_productos"]: producto for producto in lista_stock}
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_json}'. Verifique la ruta y vuelva a intentarlo.")
        return {}
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo '{archivo_json}': {e}")
        return {}


# Función para salir
def salir() -> None:
    """
    Pre: No hay condiciones previas.
    Post: Sale del programa.
    """
    print("Saliendo...")
    exit()


# Mostrar opciones principales
def mostrar_opciones():
    limpiar_pantalla()
    opciones = [
        {"id": "1", "descripcion": "Cargar Compra", "accion": cargar_compra},
        {"id": "2", "descripcion": "Ver compras", "accion": ver_compras},
        {"id": "3", "descripcion": "Ver descuento del Día", "accion": ver_descuento},
        {"id": "4", "descripcion": "Realizar Cierre de caja", "accion": cierre_caja},
        {"id": "5", "descripcion": "Salir", "accion": salir}    
    ]

    # Mostrar opciones con tabulate
    print(
        tabulate(
            [[opcion["id"], opcion["descripcion"]] for opcion in opciones],
            headers=["Opción", "Descripción"],
            tablefmt="fancy_grid",
            colalign=("center", "left"),
        )
    )

    return opciones


# Función principal
def main() -> None:
    """
    Pre: Los archivos CSV y JSON deben estar disponibles y ser válidos.
    Post: Ejecuta el programa, cargando los productos y el stock, y mostrando el menú principal.
    """
    archivo_csv = "archivos/csv/productos_50.csv"
    archivo_json = "archivos/json/json_productos_stock.json"

    # Verificar si los archivos se cargan correctamente
    if not cargar_productos_desde_csv(archivo_csv):
        print("Error crítico: No se pudieron cargar los productos del archivo CSV. El programa no se ejecutará.")
        return

    stock = cargar_stock_desde_json(archivo_json)
    if not stock:
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


# Iniciar la ejecución del programa
if __name__ == "__main__":
    main()
