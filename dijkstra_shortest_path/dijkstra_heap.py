class dijkstraHeap:
    def __init__(self, nodes):
        
        self.heapindex = {}
        self.heap = []
        i = 0
        for node in nodes:
            self.heapindex[node]=i
            self.heap.append((node, 1000000))
            i += 1
        
    def heap_replace(self, node, score):
        self.heap[self.heapindex[node]]= (node, score)
        while self.heapindex[node] != 0 and score < self.parent_nodescore(node)[1]:
            self.heap_bubbleup(node, score)

    def parent_index(self, node):
        return (self.heapindex[node]+1)//2 - 1
        
    def parent_nodescore(self, node):
        return self.heap[self.parent_index(node)]
        
    def heap_bubbleup(self, node, score):
        parent, parentscore = self.parent_nodescore(node)
        hold1 = self.heapindex[node]
        self.heapindex[node] = self.parent_index(node)
        self.heapindex[parent] = hold1
        self.heap[hold1] = (parent,parentscore)
        self.heap[self.heapindex[node]] = (node, score)
        
    def extract_min(self):
        min = self.heap[0]
        del self.heapindex[min[0]]
        node, score = self.heap.pop()
        if self.heapindex != {}:
            self.heap[0] = (node, score)
            self.heapindex[node] = 0
            child_chosen = self.smaller_child(node)
            while child_chosen and child_chosen[1]<score:
                self.heap_bubbledown(node, score, child_chosen[0])
                child_chosen = self.smaller_child(node)
        return min
                
    def child_indices(self, node):
        return [2*self.heapindex[node]+1, 2*self.heapindex[node]+2]
               
    def smaller_child(self, node):
        child_index1, child_index2 = self.child_indices(node)
        if len(self.heap)-1 >= child_index2:
            return [self.heap[child_index1], self.heap[child_index2]][self.heap[child_index1][1]>self.heap[child_index2][1]]
        elif len(self.heap)-1 >= child_index1:
            return self.heap[child_index1]
        else:
            return None
               
    def heap_bubbledown(self, node, score, child):
        hold = self.heapindex[node] 
        self.heapindex[node]=  self.heapindex[child]
        self.heapindex[child] = hold
        self.heap[hold] = self.heap[self.heapindex[node]]
        self.heap[self.heapindex[node]]=(node, score)
        


