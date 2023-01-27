import numpy as np 

map = [['4',1,0,0,1],
        [1,1,0,0,1],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,1,1,1,'5']]

def find_in_list_of_list(mylist, char):
    '''
    Function that is used to get the index acording to an especific
    element
        Recovered from: Stack Overflow 
    '''
    for sub_list in mylist:
        if char in sub_list:
            ubicar = mylist.index(sub_list), sub_list.index(char)
            return (ubicar)
    raise ValueError("'{char}' is not in list".format(char = char))

def pushFronteirs ( stack, X, Y, direc ):
    """
        Función para verificar que los índex se encuentren dentro de los límites
        del tamaño del array.
        Parámetros:
            stack: Fronteras
            X: Número de lista
            Y: Posición en lista de lista
        Returns:
            stack
    """
    limit = len(map)
    if ( X > -1 and X < limit ) and ( Y > -1 and Y < limit ):
        if (X,Y) not in stack:
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

    # Left
    X = ogX
    Y = ogY - 1
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y, 'left')

    # Up
    X = ogX - 1 
    Y = ogY
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y, 'up')

    # Right
    X = ogX
    Y = ogY + 1
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y, 'right')

    # Down
    X = ogX + 1
    Y = ogY
    if (X,Y) not in visited:
        pushFronteirs(fronteirs, X, Y, 'down')

    return fronteirs

def heuristics (map,actualNode):
    '''
    Function that is used to determin the heuristics acording to the actual 
    position vs the final position 
    '''
    end = find_in_list_of_list(map, '5')
    x1 = end[1]    
    y1 = actualNode[0]

    x2 = actualNode[1]
    y2 = end[0]
    
    x = x2 - x1
    y = y2 - y1

    h = (x + y) -1 * min(x,y)
    #print(h,'h')
    return h

def AStar( map, actualPos, visited, fronteirs,rode ):
    '''
        Función para algoritmo Star * Search.
        Parámetros:
            map: Array con mapa
            actualPos: posición (X, Y)
            visited: Array con los nodos visitados
            fronteirs: Array con los nodos "frontera"
            rode: Camino a tomar 
    '''
    temp =[]
    #print( 'actualPos: ', actualPos)

    visited.append(actualPos)
    #print( 'visited: ', visited)

    findFronteirs(actualPos, fronteirs, visited)
    #print('fronteirs: ',fronteirs)
    
    for i in range(len(fronteirs)):
        NextPos = fronteirs[i]
        Calc = heuristics(map,NextPos)
        temp.append(Calc)

    # Gets the value of the smaller heuristic
    minVal = np.min(temp)

    # Finds the frontier based on the heuristic
    indexMV = temp.index(minVal)
    node = fronteirs[indexMV]

    #Checks if a node is already in the path and if not it append it 
    if node not in rode:
        rode.append(node)

    return None

def convert_to_int(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            val =  map[i][j] = int(map[i][j])
    return val


visited = []
fronteirs = []
rode = []

startPosition = find_in_list_of_list(map, '4')

actualPos = startPosition

while map[actualPos[0]][actualPos[1]] != '5':
    AStar(map, actualPos, visited, fronteirs,rode)
    if len(fronteirs) > 0:
        actualPos = fronteirs.pop()

    #print('finalPos: ', actualPos)
    #print('value: ', map[actualPos[0]][actualPos[1]])
print(rode, 'camino' )

#Change values of the original matrix 
for i in range(len(rode)):
    coords =rode[i]
    x = coords[0]
    y = coords[1]
    map[x][y] =  8
    
convert_to_int(map)

for i in map:
    print(i)

