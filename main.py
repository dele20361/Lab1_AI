from BFS import AlgorithmBFS
from DFS import AlgorithmDFS
from AStarEuclidian import EuclidianAStar
from AStarManhattan import AlgorithmManhattan
from arrayProccesing import ArrayToImage, ImageSetup

import Algorithms

wantToContinue = True
mapa = ImageSetup('maze200x200.png')
mapa = [['4',1,0,0,0,0,0,0,0,0,0,1],
        [1,1,0,0,0,0,0,0,0,0,1,1],
        [0,1,1,1,1,1,0,0,0,1,0,0],
        [1,1,1,1,1,1,0,0,0,0,1,1],
        [1,1,1,1,1,1,1,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,0,1,1,1,'5']]

opc = input('''
1. BFS
2. DFS
3. A* con primera heurística
4. A* con segunda heurística

Seleccione el algoritmo: 
''')

match opc:
    case '1':
        bfs = AlgorithmBFS(mapa)
        mapBFS = bfs.main()
        ArrayToImage(mapBFS, 'mapBFS.png')
    case '2':
        dfs = AlgorithmDFS(mapa)
        mapDFS = dfs.main()
        ArrayToImage(mapDFS, 'mapDFS.png')
    case '3':
        euclidianA = EuclidianAStar(mapa)
        mapEuclidianA = euclidianA.main()
        ArrayToImage(mapEuclidianA, 'mapEuclidianA.png')
    case '4':
        manhattan = AlgorithmManhattan(mapa)
        mapManhattan = manhattan.main()
        ArrayToImage(mapManhattan, 'mapManhattan.png')

print('\n\nEn tu carpeta se encuentra el mapa generado! :)')