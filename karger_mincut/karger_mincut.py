from numpy import random
from numpy import log
from UnionFind import *
import copy
import time

edges = []
with open("kargerMinCut.txt") as f:
    for line in f:
        spl = line.split()
        vertex = int(spl[0])
        adjacents = spl[1:]
        adjacents = list(map(int, adjacents))
        new_edges = []
        for neighbor in adjacents:
            new_edges.append([vertex, neighbor])
        edges = edges + new_edges


def MonteCarlo_karger(edges, nodecount):
    #repeat = (nodecount**2)*log(nodecount)
    repeat = 300
    j = 0
    mincut = nodecount**2
    while j < repeat:
        edgescopy = copy.copy(edges)

        g = UnionFind()
        for i in range(1, 201):
            g.__getnode__(i)

        mergecount = 0
        while mergecount < nodecount-2:
            if g.unite(edgescopy.pop(random.choice(range(len(edgescopy))))):
                mergecount += 1
        
        crosses = 0
        for nodepair in edgescopy:
            if not g.find(nodepair):
                crosses += 1
        
        if mincut > crosses/2:
            mincut = crosses/2
        
        j += 1
    
    return mincut

start = time.time()
print(MonteCarlo_karger(edges,200))
end = time.time()
print(end - start)
        