from inspect import stack
from cv2 import findContours
import pandas as pd

map = [['*',1,0,0,1],
        [1,1,0,0,1],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,1,1,1,'x']]

def find_in_list_of_list( mylist, char ):
    """
        Tomado de: Stack Over Flow
    """
    for sub_list in mylist:
        if char in sub_list:
            return (mylist.index(sub_list), sub_list.index(char))
    raise ValueError("'{char}' is not in list".format(char = char))

def DepthFistSearch( map, actualPos, visited, fronteirs ):
    '''
        Función para algoritmo Depth First Search.
        Parámetros:
            map: Array con mapa
            actualPos: posición (X, Y)
            visited: Array con los nodos visitados
            fronteirs: Array con los nodos "frontera"
        Returns:
            map con el camino marcado.
    '''
    print( 'actualPos: ', actualPos)
    visited.append(actualPos)
    print( 'visited: ', visited)
    findFronteirs(actualPos, fronteirs, visited)

    print('fronteirs: ',fronteirs)

    return map

def pushFronteirs ( stack, X, Y ):
    """
        Función para verificar que los índex se encuentren dentro de los límites
        del tamaño del array.
        Parámetros:
            stack: Fronteras
            X: Posición X
            Y: Posición Y
        Returns:
            stack
    """
    limit = len(map)
    if ( X > -1 and X < limit ) and ( Y > -1 and Y < limit ):
        if map[X][Y] != 0:
            stack.append((X,Y))

    return stack

def findFronteirs ( actualNode, fronteirs, visited ):
    '''
        Para ver que nodos son 1 a su al rededor siempre tomando.
        Parámetros:
            actualNode: Nodo visitado
            visited: Nodos visitados
            fronteirs
        Returns:
            fronteirs actualizada
    '''
    ogX = actualNode[0]
    ogY  = actualNode[1]


    # Down
    X = ogX
    Y = ogY + 1
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y)

    # Right
    X = ogX + 1
    Y = ogY
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y)

    # Up
    X = ogX
    Y = ogY - 1
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y)

    # Left
    X = ogX - 1
    Y = ogY
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y)


    return fronteirs
        

startPosition = find_in_list_of_list(map, '*')
visited = []
fronteirs = []

actualPos = startPosition

while map[actualPos[0]][actualPos[1]] != 'x':
    DepthFistSearch(map, actualPos, visited, fronteirs)
    if len(fronteirs) > 0:
        actualPos = fronteirs.pop()

    print('finalPos: ', actualPos)
    print('value: ', map[actualPos[0]][actualPos[1]])