

#using two balanced trees to do this operations for a stack class
#main challenge is about how to track the max and last element, because normal tracking will lead to O(N) solution
#and we want to optimise, s8irely. 

#one tree is pushing stack
#and the other tree is sorted by values 
#and each elemtn also needs a aunique elemtn id 

from sortedcontainers import SortedList 

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.values = SortedList()
        self.count = 0
    
    def push(self,val):
        self.stack.add((self.count,val))
        self.values.add((val,self.count))
        self.count += 1

    def pop(self):
        ind, val = self.stack.pop()
        self.values.remove((val,ind))
        return val 

    def top(self):
        return self.stack[-1][1]
    
    def peekMax(self):
        return self.values[-1][0]
    
    def popMax(self):
        val,ind = self.values.pop()
        self.stack.remove((ind,val))
        return val  

#these are two balanced trees implementation but  i dont really like using this sortedList() thing 
#every operation is O(log N), spoace complex O(N). initialisationnhas time complex O(1)

#here is the same two balanced trees approach from scratch

class MaxStack2:

    def __init__(self):
        self.stack = [] #sorted by index, asc order
        self.values = [] #sorted by values, asc order
        self.count = 0
    
    def push(self,val):
        self.stack.append([self.count,val])
        #dont need to sort self.stack since it only ever appends in incrasing count anyway
        self.values.append([val,self.count])
        self.values.sort()

        self.count += 1
    
    def pop(self):
        ind,val = self.stack.pop()
        self.values.remove([val,ind]) #rmeoving corresponding pair from the values as well
        return val 

    def top(self):
        return self.stack[-1][1]
    def peekMax(self):
        return self.values[-1][0]
    def popMax(self):
        val,ind = self.values.pop()
        self.stack.remove([ind,val])
        return val


#doubly linked lists in python
#ikr 

import heapq #got to thank this module whart can i say
#its a minheap though not a maxheap
#so when you want to max use of maxheap properties like how finding the max value in a heap is O(1) time complexity
#yopu would need to actually store the negation of each entry instead!


class Node:
    def __init__(self,val,the_id):
        self.val = val 
        self.id = the_id 
        self.prev = None 
        self.next = None 
        self.removed = None  

#when you have a pointer to any node, you can unlink it with O(1) time complexity
#finding max value in a heap which is a max heap is O(1), and generic lookjip is O(n)
#and insertion is O(log n) as well as delketing the max value
    
class MaxStack:

    def __init__(self):
        self.head = Node(0,-1)
        self.tail = Node(0,-1)

        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.heap = []
        self.count = 0
    def _unlink(self,node):
        node.prev.next = node.next 
        node.next.prev = node.prev 
        node.removed = True 
    def _clean(self):
        # discard heap entries whose node was already popped from the stack
        while self.heap[0][2].removed:
            heapq.heappop(self.heap)

    def push(self, x: int) -> None:
        node = Node(x, self.count)
        self.count += 1
        last = self.tail.prev          # insert between last and tail
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        heapq.heappush(self.heap, (-x, -node.id, node))

    def pop(self) -> int:
        node = self.tail.prev
        self._unlink(node)             # stays in heap, but marked removed
        return node.val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        self._clean()
        return self.heap[0][2].val

    def popMax(self) -> int:
        self._clean()
        _, _, node = heapq.heappop(self.heap)
        self._unlink(node)             # O(1) because we hold a pointer to it
        return node.val


#this version was not actually pssing all text cases, only 164/166
#so thuis version implements lazy deletion to saveruntime

def MaxStackBetter():

    def __init__(self):
        self.stack = []
        self.heap = []
        self.removed = set() #these can hold the ids which are removed from the other structure
        self.count = 0

    def push(self,x):
        self.stack.append((x,self.count)) #adding the value and the id as such
        #then we use a heap for the next one since we want the values to be stored as max heap data strcuture
        #and negating all values since heapq is minheap nstructure

        heapq.heappush(self.heap, (-x, -self.count)) #self,coiunt is also negative here for same reason
        self.count += 1
    
    def _clean_stack(self):
        #emptying the stack after popMax removed the 
        while self.stack[-1][1] in self.removed:
            self.removed.remove(self.stack.pop()[1])
        
    def _clean_heap(self):
        while -self.heap[0][1] in self.removed:
            self.removed.remove(-heapq.heappop(self.heap)[1])
    
    def pop(self):
        self._clean_stack()
        x,i = self.stack.pop()
        self.removed.add(i)
        return x 

    def top(self):
        self._clean_stack()
        return self.stack[1][0]
    
    def peekMax(self):
        self._clean.heap()
        x,i = heapq.heappop(self.heap)
        self.renoved.add(-i)
        return -x