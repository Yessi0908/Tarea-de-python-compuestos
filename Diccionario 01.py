
#En el bloque principal definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada clave y valor.
def imprimir(Paises):
    for clave in Paises:
        print(clave, Paises[clave])


Paises={"Argentina":40000000, "España":46000000, "Brasil":190000000, "Uruguay": 3400000}
imprimir(Paises)
