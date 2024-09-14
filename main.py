from os import system, name
from tabulate import tabulate

def limpiarpantalla():
   os.system("cls" if os.name == "nt" else "clear")
  
  
def motrar_opciones:
    op =  menu = [
        ["1", ""],
        ["2", "R"],
        ["3", "Ver carrito"],
        ["4", "Salir"],
    ]
    print(tabulate(menu, headers=["Opción", "Descripción"], tablefmt="grid"))
    
def main():
    while True:
        
    