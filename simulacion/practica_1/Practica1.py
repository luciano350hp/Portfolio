
#!/usr/bin/env python
#from curses import wrapper
import curses
def lista_puntos():
    """ Retorna una lista con los pares fila-columna del .txt
        separados por coma, en String. """
    archivo = open("puntos.txt", 'r')
    lista = archivo.readlines()
    lista = list(map(lambda x: x.strip() , lista)) #Quito el '/n'.
    lista = list(filter(lambda x: (x != '') , lista)) #Filtro eliminando espacios vacios.
    archivo.close()
    return (lista) 

def lista_filas():
    """ Retorna una lista con los valores 'fila' del .txt 
	(de hasta dos digitos c/u), separados por coma, en int. """
    lista = lista_puntos()
    filas = []
    for elemento in lista:
        if not (elemento[1].isdigit()):
           filas.append(elemento[0])
        else:
           filas.append(elemento[0] + elemento[1])
    filas = list(map(lambda x: int(x) , filas)) #Transformo a int la lista String.
    return (filas) 

def lista_columnas():
    """ Retorna una lista con los valores 'columna' del .txt 
	(de hasta dos digitos c/u), separados por coma, en int. """
    lista = lista_puntos()
    columnas = []
    for elemento in lista:
        if (len(elemento) == 3):
           columnas.append(elemento[2])
        elif ((len(elemento) == 4) and (not (elemento[1].isdigit()))):
           columnas.append(elemento[2] + elemento[3])
        elif ((len(elemento) == 5)):
           columnas.append(elemento[3] + elemento[4])
        else:
           columnas.append(elemento[3])
    columnas = list(map(lambda x: int(x) , columnas)) #Transformo a int la lista String.
    return (columnas) 

def matriz():
    """ Se inicializa la matriz de  27 X 27."""
    matriz = []
    for i in range (27):
        matriz.append([0] * 27)
    return(matriz)

def imprimir():
    """ Imprime en pantalla las listas generadas del .txt. """
    lista1 = lista_puntos()
    lista2 = lista_filas()
    lista3 = lista_columnas()
    print("La lista de puntos es: ", lista1)
    print("La lista de filas es: ", lista2)
    print("La lista de columnas es: ", lista3)
    print("Ha ingresado:",len(lista1), "individuos vivos") 

def imprimir_matriz(matriz2):
    """ Imprime la matriz generada. """
    print("La matriz es: ")
    for filas in matriz2:
        print (filas)

def poner_vivos():
    """ Ingresa en la ventana los individuos vivos obtenidos del .txt.
        Se empieza el juego con 'b'.
        Se llena la matriz con la configuracion inicial del .txt.  """
    filas = lista_filas()
    columnas = lista_columnas()
    ventana = iniciar_tablero()
    matriz1 = matriz()
    curses.noecho()
    for fila, columna in zip(filas, columnas): 
        ventana.addstr(fila,columna,"X")
        matriz1[fila][columna] = "X" 
    ventana.refresh() 
    if (ventana.getch() == ord('b')):
        jugar(ventana, matriz1)
    curses.endwin()
    imprimir()
    imprimir_matriz(matriz1)


def iniciar_tablero():
    """ Se inicia el tablero de 27 X 27 vacio."""
    ventana = curses.initscr()
    for x in range (0, 27):
        for y in range (0, 27):
            ventana.addstr(x,y," ")
    ventana.border(0,0,0,0,0,0,0)
    return(ventana)

def cantidad_vecinos(matriz1, fila, columna):
    """ Retorna cantidad de vecinos de una posicion de la matriz."""
    vecinos = 0
    if matriz1[fila][columna -1] == "X":
       vecinos += 1
    if matriz1[fila][columna +1] == "X":
       vecinos += 1
    if matriz1[fila +1][columna -1] == "X":
       vecinos += 1
    if matriz1[fila +1][columna] == "X":
       vecinos += 1
    if matriz1[fila +1][columna +1] == "X":
       vecinos += 1
    if matriz1[fila -1][columna -1] == "X":
       vecinos += 1
    if matriz1[fila -1][columna] == "X":
       vecinos += 1
    if matriz1[fila -1][columna +1] == "X":
       vecinos += 1
    return (vecinos)            

def calcular(matriz3):
    """ Genera una matriz aplicandole las reglas del Juego de la Vida. """
    matriz2 = matriz()
    for fila in range (1, 26):
        for columna in range (1, 26):
            vecinos = cantidad_vecinos(matriz3, fila, columna)
            if matriz3[fila][columna] == 'X':
                if not (vecinos == 2 or vecinos == 3):
                    matriz2[fila][columna] = 0
                else:
                    matriz2[fila][columna] = 'X'
            else:
                if (vecinos == 3):
                    matriz2[fila][columna] = "X"
    return(matriz2)

def jugar(ventana1, matriz1):
    """ Genera los ciclos del juego de la vida segun
        los puntos ingresados y los siguientes
        que se van generando ."""
    curses.noecho() 
    ventana1.nodelay(True)
    ventana1.refresh()
    while (ventana1.getch() != ord('q')):
        matriz2 = calcular(matriz1)
        for fila in range (1, 26):
            for columna in range (1, 26):
                if matriz2[fila][columna] == 'X':
                    ventana1.addstr(fila, columna, 'X')
                else:
                    ventana1.addstr(fila, columna, " ")
        ventana1.refresh() 
        curses.delay_output(400)
        matriz1 = matriz2
    curses.endwin()
    imprimir_matriz(matriz1) #Imprime la ultima matriz que se generó

def main():
    """ Llama a poner_vivos y la misma se encarga
        de llamar al resto de las funciones. """
    poner_vivos()
main()
