from BFS import AlgorithmBFS
from DFS import AlgorithmDFS
from AStarEuclidian import EuclidianAStar
from AStarManhattan import AlgorithmManhattan
import Algorithms

mapa = [['4',1,0,0,1],
        [1,1,0,0,1],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,1,1,1,'5']]

bfs = AlgorithmBFS(mapa)
mapBFS = bfs.main()
print(mapBFS)

dfs = AlgorithmDFS(mapa)
mapDFS = dfs.main()
print(mapDFS)

euclidianA = EuclidianAStar(mapa)
mapEuclidianA = euclidianA.main()
print(mapEuclidianA)

manhattan = AlgorithmManhattan(mapa)
mapManhattan = manhattan.main()
print(mapManhattan)