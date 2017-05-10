# SccDigraph class inplemented to efficiently compute the sizes of SCCs
class SccDigraph:
    def __init__(self):
        self.adjacents = {}
        self.rev_adjacents = {}
        self.explored = {}
        self.rev_explored = {}
        self.finish = {}

    def add_vertex(self,vertex):
        self.adjacents[vertex] = []
        self.rev_adjacents[vertex] = []
        self.explored[vertex] = False
        self.rev_explored[vertex] = False
        self.finish[vertex] = None

    def add_edge(self, edge):
        self.adjacents[edge[0]].append(edge[1])
        self.rev_adjacents[edge[1]].append(edge[0])
        
    def rev_dfsloop(self): 
        t = 1
        for vertex in self.adjacents:
            stack = [vertex]
            while stack:
                current = stack.pop()
                if not self.rev_explored[current]:
                    self.rev_explored[current]=True
                    stack.append(current)
                    for neighbor in self.rev_adjacents[current]:
                        if not self.rev_explored[neighbor]:
                            stack.append(neighbor)
                else:
                    if self.finish[current] == None:
                        self.finish[current] = t
                        t += 1
                        
    def scc_counts(self):
        counts = []
        order = [None]*len(self.finish)
        for vertex in self.finish:
            order[-self.finish[vertex]] = vertex
        for vertex in order:
            if not self.explored[vertex]:
                self.explored[vertex]=True
                count = 1
                stack = [vertex]
                while stack:
                    for neighbor in self.adjacents[stack.pop()]:
                        if not self.explored[neighbor]:
                            self.explored[neighbor]=True
                            stack.append(neighbor)
                            count += 1
                counts.append(count)
        counts.sort()
        return counts
                
                        
                    
        
# graph creation based on edges listed in scc.txt                            
vertices = range(1,875715)         
         
edges = []
with open("scc.txt") as f:
    for line in f:
        spl = line.split()
        edge = [int(spl[0]), int(spl[1])]
        edges.append(edge)
        
g = SccDigraph()
for vertex in vertices:
    g.add_vertex(vertex)
    
for edge in edges:
    g.add_edge(edge)    
    





        