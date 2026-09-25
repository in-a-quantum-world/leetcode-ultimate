import random

class MinHeap:
    def __init__(self):
        self.data = [] # the tree

    def _parent(self,i):
        return (i-1)//2
    
    def _left(self,i):
        return 2*i + 1
    
    def _right(self,i):
        return 2*i + 2

    def push(self,val):
        self.data.append(val)
        self._bubble_up(len(self.data)-1)
    
    def pop(self):
        if not self.data: #emtpy heap
            raise IndexError("pop from empty heap")
        smallest = self.data[0] #first item
        last = self.data.pop()

        if self.data: #if anyting is left, this needs to be reassigned 
            self.data[0] = last 
            self._bubble_down(0) #bubble down

        return smallest

    def peek(self):
        return self.data[0] #return min
    
    def __len__(self):
        return len(self.data)

    def _bubble_up(self,i):
        while i > 0:
            p = self.parent(i)
            if self.data[i] < self.data[p]: #if current is smaller,
            #then current needs to be swapped with aprent as current should be 
            # the root of the subtree, to stick to the rules of heaps. 
                self.data[i],self.data[p] = self.data[p], self.data[i]
                i = p 
            else:
                break

    def _bubble_down(self,i):
        n = len(self.data)
        while True: #tis 
            smallest = i     
            l = self._left(i)
            r  =self._right(i)
            #since we are bubbling down
            #swapping will need to consdier both left and right child nodes 
            # as opposed to just one 

            if l < n and self.data[l] < self.data[smallest]:
                smallest = l 
            if r < n and self.data[r] < self.data[smallest]:
                smallest = r
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]

            i = smallest #swap



#testing

if __name__ == '__main__':
    h = MinHeap()
    for x in [5, 3, 8, 1]:
        h.push(x)
        print("after push", x, "->", h.data)
 
    print("pop ->", h.pop(), " heap now", h.data)
 
    # self-check: popping everything must give the numbers in sorted order
    for _ in range(1000):
        nums = [random.randint(-50, 50) for _ in range(random.randint(0, 30))]
        mine = MinHeap()
        for x in nums:
            mine.push(x)
        assert [mine.pop() for _ in range(len(nums))] == sorted(nums)
    print("all random tests passed")