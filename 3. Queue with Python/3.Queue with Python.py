#Queue use in our day to day life : ticket counter, place order, stock price....
#First in First Out : FIFO

from collections import deque

class Queue:
    def __init__(self) :   #declear queue
        self.buffer = deque()

    def enqueue(self,val):  #add element
        self.buffer.appendleft(val)
    
    def dequeue(self): #remove element
        self.buffer.pop()

    def show(self): #show element
        return print(f'{self.buffer}')
    
    def size(self): #size of queue
        return print(f'Size of queue=> {len(self.buffer)}')
    
    def is_empty(self): #check empty or not
        return print(f'Empty of Queue => {len(self.buffer) == 0 }')
    

obj_queue = Queue()

obj_queue.enqueue(1)
obj_queue.enqueue(2)
obj_queue.enqueue(3)
obj_queue.enqueue(4)
obj_queue.enqueue(5)
obj_queue.show()
obj_queue.size()
obj_queue.is_empty()
obj_queue.dequeue()
obj_queue.dequeue()
obj_queue.dequeue()
obj_queue.dequeue()
obj_queue.dequeue()
obj_queue.show()
