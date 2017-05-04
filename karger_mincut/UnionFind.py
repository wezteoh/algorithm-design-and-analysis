

class UnionFind:
    def __init__(self):
        self.id = {}
        self.weight = {}

    def __getnode__(self, node):
        if not node in self.id:
            self.id[node] = node
            self.weight[node] = 1
            
    def root(self, node):
        while self.id[node] != node:
            self.id[node] = self.id[self.id[node]]
            node = self.id[node]
        return node

    def unite(self, nodepair):
        root1 = self.root(nodepair[0])
        root2 = self.root(nodepair[1])
        if root1 != root2:
            if self.weight[root1] < self.weight[root2]:
                self.id[root1] = self.root(root2)
                self.weight[root2] += self.weight[root1]
            else: 
                self.id[root2] = self.root(root1)
                self.weight[root1] += self.weight[root2]
            return True
        
        else:
            return False
            
                
    def find(self, nodepair):
        return self.root(nodepair[0])== self.root(nodepair[1])


    


    

        

    