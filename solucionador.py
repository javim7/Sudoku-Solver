__author__ = "Javier Mombiela"
__copyright__ = "Copyright 2021, Sudoku Solver"
__credits__ = ["Tech with Tim"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Javier Mombiela"
__email__ = "rjmombiela@gmail.com"
__status__ = "Production"

#creacion del tablero de sudoku por medio de una lista de listas
#los " " son los espacios vacios del tablero
tablero = [
    [7,8," ",4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#funcion para poder imprimir el tablero
def imprimir_tablero(tab):

    for i in range(len(tab)): #imprimir las lineas horizontales por cada 3 lineas
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - ")

        for j in range(len(tab[0])): #imprimir las lineas verticales por cada 3 columnas
            if j % 3 == 0 and j!=0:
                print(" | ", end="")

            if j == 8: #verficar si ya estamos en la ultima posicion
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end=" ")

#funcion para poder encontrar un espacio vacio
def econtrar_vacio(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                return (i,j) # retornar la fila y columna
            
imprimir_tablero(tablero)