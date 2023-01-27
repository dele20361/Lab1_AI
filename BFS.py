#from inspect import stack
#from cv2 import findContours
#import pandas as pd

from Algorithms import Algorithms

class AlgorithmBFS():

    def __init__(self, map):
        self.map = map

    def find_in_list_of_list( self, mylist, char ):
        """
            Tomado de: Stack Overflow
        """
        for sub_list in mylist:
            if char in sub_list:
                return (mylist.index(sub_list), sub_list.index(char))
        raise ValueError("'{char}' is not in list".format(char = char))

    def BreadthFistSearch( self, map, actualPos, visited, fronteirs ):
        '''
            Función para algoritmo Breadth First Search.
            Parámetros:
                map: Array con mapa
                actualPos: posición (X, Y)
                visited: Array con los nodos visitados
                fronteirs: Array con los nodos "frontera"
            Returns:
                map con el camino marcado.
        '''
        visited.append(actualPos)
        AlgorithmBFS.findFronteirs(self, actualPos, fronteirs, visited)

        return self.map

    def pushFronteirs ( self, stack, X, Y, direc ):
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
        limit = len(self.map)
        if ( X > -1 and X < limit ) and ( Y > -1 and Y < limit ):
            if (X,Y) not in stack:
                if self.map[X][Y] != 0:
                    stack.append((X,Y))

        return stack

    def findFronteirs ( self, actualNode, fronteirs, visited ):
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
            AlgorithmBFS.pushFronteirs(self, fronteirs, X, Y, 'left')

        # Up
        X = ogX - 1 
        Y = ogY
        if (X,Y) not in visited:
            AlgorithmBFS.pushFronteirs(self, fronteirs, X, Y, 'up')

        # Right
        X = ogX
        Y = ogY + 1
        if (X,Y) not in visited:
            AlgorithmBFS.pushFronteirs(self, fronteirs, X, Y, 'right')

        # Down
        X = ogX + 1
        Y = ogY
        if (X,Y) not in visited:
            AlgorithmBFS.pushFronteirs(self, fronteirs, X, Y, 'down')

        return fronteirs

    def invert (self, map):
        startPosition = AlgorithmBFS.find_in_list_of_list(self, self.map, '5')
        visited = []
        fronteirs = []
        rode = []
        i=0

        actualPos = startPosition

        while self.map[actualPos[0]][actualPos[1]] != '4':
            AlgorithmBFS.BreadthFistSearch(self, self.map, actualPos, visited, fronteirs)
            if len(fronteirs) > 0:
                actualPos = fronteirs.pop()

                rode.append(actualPos)
        return rode  

    def convert_to_int(self, map):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                val =  map[i][j] = int(self.map[i][j])
        return val
            
    def main( self ):
        startPosition = AlgorithmBFS.find_in_list_of_list(self, self.map, '4')
        visited = []
        fronteirs = []
        path =[]
        path1 = []
        path2 = AlgorithmBFS.invert(self, self.map)

        i = 0

        actualPos = startPosition

        while self.map[actualPos[0]][actualPos[1]] != '5':
            AlgorithmBFS.BreadthFistSearch(self, self.map, actualPos, visited, fronteirs)
            if len(fronteirs) > 0:
                actualPos = fronteirs.pop(0)
            path1.append(actualPos)

        for i in path1:
            for j in path2:
                if i==j:
                    path.append(j)

        for i in range(len(path)):
            coords =path[i]
            x = coords[0]
            y = coords[1]
            self.map[x][y] = 8

        AlgorithmBFS.convert_to_int(self, self.map)

        return self.map