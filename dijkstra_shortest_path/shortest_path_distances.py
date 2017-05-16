from dijkstra_heap import *

adjacents_dict = {}
with open("dijkstraData.txt") as f:
    for line in f:
        spl = line.split()
        node = int(spl[0])
        adjacents_dict[node]=[]
        adjacents = spl[1:]
        for neighbor in adjacents:
            adjacents_dict[node].append(tuple(map(int, neighbor.split(','))))

sp_distance = []
h = dijkstraHeap(range(1,201))
h.heap_replace(1,0)
sp_distance.append(h.extract_min())
while len(sp_distance)<200:
    for neighbor in adjacents_dict[sp_distance[-1][0]]:
        if neighbor[0] in h.heapindex:
            greedy_score = neighbor[1] + sp_distance[-1][1]
            if greedy_score < h.heap[h.heapindex[neighbor[0]]][1]:
                h.heap_replace(neighbor[0],greedy_score)
    sp_distance.append(h.extract_min())    

ordered = [None]*200
for node_distance in sp_distance:
    ordered[node_distance[0]-1] = node_distance