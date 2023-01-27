from BFS import AlgorithmBFS
import Algorithms

mapa = [['4',1,0,0,1],
        [1,1,0,0,1],
        [0,1,1,1,0],
        [1,1,1,1,1],
        [0,1,1,1,'5']]

bfs = AlgorithmBFS(mapa)
print(bfs.main())