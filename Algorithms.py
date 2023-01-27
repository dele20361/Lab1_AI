
from abc import ABC, abstractmethod


class Algorithms(ABC):

    @abstractmethod
    def find_in_list_of_list( self, mylist, char ):
        pass

    @abstractmethod
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
        pass

    @abstractmethod
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
        pass
