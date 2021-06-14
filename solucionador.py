__author__ = "Javier Mombiela"
__copyright__ = "Copyright 2021, Sudoku Solver"
__credits__ = ["Tech with Tim"]
__license__ = "GPL"
__version__ = "2.0.1"
__maintainer__ = "Javier Mombiela"
__email__ = "rjmombiela@gmail.com"
__status__ = "Production"

#creacion del tablero de sudoku por medio de una lista de listas
#las x's son los espacios vacios del tablero
tablero = [
    [7,8,"x",4,"x","x",1,2,"x"],
    [6,"x","x","x",7,5,"x","x",9],
    ["x","x","x",6,"x",1,"x",7,8],
    ["x","x",7,"x",4,"x",2,6,"x"],
    ["x","x",1,"x",5,"x",9,3,"x"],
    [9,"x",4,"x",6,"x","x","x",5],
    ["x",7,"x",3,"x","x","x",1,2],
    [1,2,"x","x","x",7,4,"x","x"],
    ["x",4,9,2,"x",6,"x","x",7]
]
"""
tablero = [
    [1,"x","x",4,8,9,"x","x",6],
    [7,3,"x","x",5,"x","x",4,"x"],
    [4,6,"x","x","x",1,2,9,5],
    [3,8,7,1,2,"x",6,"x","x"],
    [5,"x",1,7,"x",3,"x","x",8],
    ["x",4,6,"x",9,5,7,1,"x"],
    [9,1,4,6,"x","x","x",8,"x"],
    ["x",2,"x","x",4,"x","x",3,7],
    [8,"x",3,5,1,2,"x","x",4]
]"""

#funcion para poder imprimir el tablero
def imprimir_tablero(tab):

    #Parametros:
    #    tab (lista):La lista de listas que crea el tablero.

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

    #Retorna la fila y columna del espacio vacio.

    #Parametros:
    #    tab (lista):La lista de listas que crea el tablero.

    #Retorna:
    #    (i,j):fila y columna del espacio vacio.  
    #    None: si no hay espacios vacios restantes

    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == "x":
                return (i,j) # retornar la fila y columna

    return None

#funcion para ver si el numero ingresado es valido o no
def es_valido(tab, num, pos):

    #Retorna booleano para ver si el numer es valido o no.

    #Parametros:
    #    tab (lista):La lista de listas que crea el tablero.
    #    num (int): el numero que se probara
    #    pos: la posicion del espacio vacio encontrado

    #Retorna:
    #    False: si el numero no es valido.  
    #    True: si el numero si es valido.

    #revisar fila
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False

    #revisar columna
    for i in range(len(tab)):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False

    #revisar cada caja de 3x3
    caja_x = pos[1] // 3
    caja_y = pos[0] //3

    #for loop para poder llegar al elemento correcto de todo el tablero
    for i in range (caja_y*3, caja_y*3 + 3):
        for j in range (caja_x*3, caja_x*3 + 3):
            if tab[i][j] == num and (i,j) != pos:
                return False

    #retornar True si todas las revisiones fueron exitosas
    return True

#funcion para resolver el tablero
def resolver(tab):

     #Retorna booleano para ver si el tablero se soluciono o no.

    #Parametros:
    #    tab (lista):La lista de listas que crea el tablero.

    #Retorna:
    #    False: si la solucion no se ha encontrado.  
    #    True: si la solucion se logro encontrar.

    #empieza algoritmo de recursion 
    encontrar = econtrar_vacio(tab)
    if not encontrar:
        return True
    else:
        fila, columna = encontrar

    #iterar valores e intentar agregar un entero del 1 al 9
    for i in range(1,10):
        if es_valido(tab, i, (fila, columna)): #ver si el entero es valido por medio de nuestra funcion anterior
            tab[fila][columna] = i #si es valido ingresar el entero al tablero 

            if resolver(tab): #if para hacer un ciclo donde se intenten agregar los numeros al espacio vacio
                return True

            tab[fila][columna] = "x" #si no se logre lo anterior, se resetea el valor, para hacer el backtracking

    return False

#llamar las funcioenes
print("\n--------Tablero Original-------")
imprimir_tablero(tablero)
print("--------------------------------")
resolver(tablero)
print("\n---------Tablero Final---------")
imprimir_tablero(tablero)
print("--------------------------------")


    
