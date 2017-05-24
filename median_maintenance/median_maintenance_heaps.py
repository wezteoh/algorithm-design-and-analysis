class MinHeap():
    def __init__(self):
        self.heap = []
        self.heapindex = {}
        
    def insert(self, num):
        self.heapindex[num]=len(self.heap)
        self.heap.append(num)
        while self.heapindex[num] != 0 and num < self.heap[self.parent_index(num)]:
            self.bubble_up(num)
    
    def parent_index(self, num):
        return (self.heapindex[num]+1)//2 - 1
    
    def bubble_up(self, num):
        parent = self.heap[self.parent_index(num)]
        hold1 = self.heapindex[num]
        self.heapindex[num] = self.parent_index(num)
        self.heapindex[parent] = hold1
        self.heap[hold1] = parent
        self.heap[self.heapindex[num]] = num
    
    def extract_min(self):
        min = self.heap[0]
        del self.heapindex[min]
        num = self.heap.pop()
        if self.heapindex != {}:
            self.heap[0] = num
            self.heapindex[num] = 0
            child_chosen = self.smaller_child(num)
            while child_chosen and child_chosen<num:
                self.heap_bubbledown(num, child_chosen)
                child_chosen = self.smaller_child(num)
        return min
                
    def child_indices(self, num):
        return [2*self.heapindex[num]+1, 2*self.heapindex[num]+2]
               
    def smaller_child(self, num):
        child_index1, child_index2 = self.child_indices(num)
        if len(self.heap)-1 >= child_index2:
            return [self.heap[child_index1], self.heap[child_index2]][self.heap[child_index1]>self.heap[child_index2]]
        elif len(self.heap)-1 >= child_index1:
            return self.heap[child_index1]
        else:
            return None
               
    def heap_bubbledown(self, num, child):
        hold = self.heapindex[num] 
        self.heapindex[num]=  self.heapindex[child]
        self.heapindex[child] = hold
        self.heap[hold] = self.heap[self.heapindex[num]]
        self.heap[self.heapindex[num]] = num


class MaxHeap():
    def __init__(self):
        self.heap = []
        self.heapindex = {}
        
    def insert(self, num):
        self.heapindex[num]=len(self.heap)
        self.heap.append(num)
        while self.heapindex[num] != 0 and num > self.heap[self.parent_index(num)]:
            self.bubble_up(num)
    
    def parent_index(self, num):
        return (self.heapindex[num]+1)//2 - 1
    
    def bubble_up(self, num):
        parent = self.heap[self.parent_index(num)]
        hold1 = self.heapindex[num]
        self.heapindex[num] = self.parent_index(num)
        self.heapindex[parent] = hold1
        self.heap[hold1] = parent
        self.heap[self.heapindex[num]] = num
    
    def extract_max(self):
        max = self.heap[0]
        del self.heapindex[max]
        num = self.heap.pop()
        if self.heapindex != {}:
            self.heap[0] = num
            self.heapindex[num] = 0
            child_chosen = self.bigger_child(num)
            while child_chosen and child_chosen > num:
                self.heap_bubbledown(num, child_chosen)
                child_chosen = self.bigger_child(num)
        return max
                
    def child_indices(self, num):
        return [2*self.heapindex[num]+1, 2*self.heapindex[num]+2]
               
    def bigger_child(self, num):
        child_index1, child_index2 = self.child_indices(num)
        if len(self.heap)-1 >= child_index2:
            return [self.heap[child_index1], self.heap[child_index2]][self.heap[child_index1]<self.heap[child_index2]]
        elif len(self.heap)-1 >= child_index1:
            return self.heap[child_index1]
        else:
            return None
               
    def heap_bubbledown(self, num, child):
        hold = self.heapindex[num] 
        self.heapindex[num]=  self.heapindex[child]
        self.heapindex[child] = hold
        self.heap[hold] = self.heap[self.heapindex[num]]
        self.heap[self.heapindex[num]] = num


class DoubleHeap():
    def __init__(self):
        self.highheap = MinHeap()
        self.lowheap = MaxHeap()
        self.highcount = 0
        self.lowcount = 0
        
    def insert(self,num):
        if self.lowcount + self.highcount == 0:
            self.lowheap.insert(num)
            self.lowcount += 1
        elif num < self.lowheap.heap[0]:
            self.lowheap.insert(num)
            self.lowcount += 1
        else:
            self.highheap.insert(num)
            self.highcount += 1
        self.balance()
        
            
    def balance(self):
        while self.lowcount - self.highcount > 1:
             self.highheap.insert(self.lowheap.extract_max())
             self.lowcount -= 1
             self.highcount += 1
        
        while self.highcount - self.lowcount >= 1:
             self.lowheap.insert(self.highheap.extract_min())
             self.lowcount += 1
             self.highcount -= 1 
        
    def get_median(self):
        return self.lowheap.heap[0]
            



num_stream = []
with open("Median.txt") as f:
    for line in f:
        num = line.split()[0]
        num_stream.append(int(num))

h = DoubleHeap()
median_sum = 0
for num in num_stream:
    h.insert(num)
    median_sum += h.get_median()
    
        
        
        