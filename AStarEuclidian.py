from cv2 import Algorithm
import numpy as np 

class EuclidianAStar(Algorithm):

    def __init__(self, map):
        self.map = map

    def find_in_list_of_list(self, mylist, char):
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
            EuclidianAStar.pushFronteirs(self, fronteirs, X, Y, 'left')

        # Up
        X = ogX - 1 
        Y = ogY
        if (X,Y) not in visited:
            EuclidianAStar.pushFronteirs(self, fronteirs, X, Y, 'up')

        # Right
        X = ogX
        Y = ogY + 1
        if (X,Y) not in visited:
            EuclidianAStar.pushFronteirs(self, fronteirs, X, Y, 'right')

        # Down
        X = ogX + 1
        Y = ogY
        if (X,Y) not in visited:
            EuclidianAStar.pushFronteirs(self, fronteirs, X, Y, 'down')

        return fronteirs

    def heuristics (self, map,actual):
        '''
        Funcrion that is used to determin the heuristics acording to the actual 
        position vs the final position 
        '''
        end = EuclidianAStar.find_in_list_of_list(self, self.map,'5')

        #Position of the near 1 
        x1 = actual[0]
        y1 = actual[1]

        #Position of the final symbol  
        x2 = end[0]
        y2 = end[1]

        #Heuristics calculation 
        x = x2 - x1
        y = y2 - y1
        
        h = x + y 
        H = round(np.sqrt(h),2) 

        return H

    def AStar( self, map, actualPos, visited, fronteirs,rode ):
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

        EuclidianAStar.findFronteirs(self, actualPos, fronteirs, visited)
        #print('fronteirs: ',fronteirs)
        
        for i in range(len(fronteirs)):
            NextPos = fronteirs[i]
            Calc = EuclidianAStar.heuristics(self, self.map, NextPos)
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

    def convert_to_int(self, map):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                val =  self.map[i][j] = int(self.map[i][j])
        return val

    def main(self):

        visited = []
        fronteirs = []
        rode = []

        startPosition = EuclidianAStar.find_in_list_of_list(self, self.map, '4')

        actualPos = startPosition

        while self.map[actualPos[0]][actualPos[1]] != '5':
            EuclidianAStar.AStar(self, self.map, actualPos, visited, fronteirs,rode)
            if len(fronteirs) > 0:
                actualPos = fronteirs.pop()

        #Change values of the original matrix 
        for i in range(len(rode)):
            coords =rode[i]
            x = coords[0]
            y = coords[1]
            self.map[x][y] =  8
            
        EuclidianAStar.convert_to_int(self, self.map)

        return self.map