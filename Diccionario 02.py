
#Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.
#Desarrollar además las funciones de:
#1) Imprimir en forma completa el diccionario
#2) Imprimir solo los artículos con precio superior a 100.

def cargar():
    Productos={}
    for x in range(5):
        Nombre=input("Escriba el nombre del producto:")
        Precio=int(input("Escriba el precio:"))
        Productos[Nombre]=Precio
    return Productos


def imprimir(Productos):
    print("Listado de todos los articulos")
    for Nombre in Productos:
        print(Nombre, Productos[Nombre])


def imprimir_mayor100(Productos):
    print("Listado de articulos con precios mayores a 100")
    for Nombre in Productos:
        if Productos[Nombre]>100:
            print(Nombre)

            
# bloque principal

Productos=cargar()
imprimir(Productos)
imprimir_mayor100(Productos)
