from os import system, name
from tabulate import tabulate
import datetime
import json

#identifica el sistema operativo
def limpiarpantalla():
   system("cls" if name == "nt" else "clear")


def mostrar_opciones():
    opciones = [
        ["1", "Cargar Compra"],
        ["2", "Ver compras"],
        ["3", "Ver descuento del Día"],
        ["4", "Generar ticket de compra"],
        ["5", "Agregar productos"],
        ["6", "Salir"]
    ]
    print(tabulate(opciones, headers=["Opción", "Descripción"], tablefmt='fancy_grid', colalign=("center", "left")))


def main():
    while True:
        limpiarpantalla() #Limpia la pantalla antes de mostrar las opciones.
        mostrar_opciones()
        usuario = input("Ingrese una opcion: ")

        if usuario == "1":
            print("Selecciono la opción 1, 'Cargar Compra'.")
            pass
        elif usuario == "2":
            print("Selecciono la opción 2, 'Ver compras'.")
            pass
        elif usuario == "3":
            print("Selecciono la opción 3, 'Ver descuento del Día'.")
            pass
        elif usuario == "4":
            print("Selecciono la opción 4, 'Generar ticket de compra'.")
            pass
        elif usuario == "5":
            print("Selecciono la opción 5, 'Agregar productos'.")
            pass
        elif usuario == "6":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

        input("\nPresione Enter para continuar. \n")  # Pausa antes de limpiar de nuevo


if __name__ == "__main__":
    main()



