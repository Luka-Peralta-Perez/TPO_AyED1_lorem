from os import system, name
from tabulate import tabulate
import datetime
import json

def cargar_compra(stock):
    # Implementar la función cargar_compra
    pass

def ver_compras():
    # Implementar la función ver_compras
    pass

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
    with open(archivo_csv, "rt", encoding="utf-8-sig") as archivo:
        productos = [linea.rstrip().split(";") for linea in archivo]

def cargar_stock_desde_json(archivo_json):
    with open(archivo_json) as f:
        return json.load(f)

def salir():
    print("Saliendo...")
    exit()

def mostrar_opciones(): 
    opciones = [
        {"id": "1", "descripcion": "Cargar Compra", "accion": cargar_compra},
        {"id": "2", "descripcion": "Ver compras", "accion": ver_compras},
        {"id": "3", "descripcion": "Ver descuento del Día", "accion": ver_descuento},
        {"id": "4", "descripcion": "Generar ticket de compra", "accion": generar_ticket},
        {"id": "5", "descripcion": "Agregar productos", "accion": agregar_productos},
        {"id": "6", "descripcion": "Salir", "accion": salir}
    ]

    print("Seleccione una opción:")
    for opcion in opciones:
        print(f"{opcion['id']}: {opcion['descripcion']}")
    
    return opciones

# Función principal del programa
def main():
    # Cargar los productos desde el archivo CSV y el stock desde JSON
    archivo_json = "json_productos_stock.json"
    archivo_csv = "productos_50.csv"
    cargar_productos_desde_csv(archivo_csv)
    stock = cargar_stock_desde_json(archivo_json)
    
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