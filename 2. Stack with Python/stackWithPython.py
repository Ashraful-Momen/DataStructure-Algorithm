#list is a dynamic array and store data in Block ways in Memory that's why use=> deque form collections.

from collections import deque

stack = deque() # declear stack 

dir(stack)
# print(dir(stack)) #list of fucntion of deque.

# print(len(stack)) # size of stack.


#Create/Add => --------------------
# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.append('d')
# stack.append('e')

# print(stack)

#Delete/pop=>--------------------
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop() #IndexError: pop from an empty deque
# print(stack)


# ----------------------------------Stack with Class --------------------------------
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def show(self):
        return print(f"Total Element of Stack=> {self.container}")
    
    def push(self,value):
        self.container.append(value)
    
    def pop(self,value):
        return self.container.pop(value)
    
    def peek(self): #show the value of last element not add/remove
        return print(f'Last Element of Stack=> {self.container[-1]}')
    
    def is_empty(self):
        return print(f'Stack is Empty=>{len(self.container)==0}')

    def size(self):
        return print(f'Size/Total Element of Stack=> {len(self.container)}')
    

obj_stack = Stack()

obj_stack.push(1)
obj_stack.push(2)
obj_stack.push(3)
obj_stack.push(4)
obj_stack.push(5)
obj_stack.peek()
obj_stack.show()
obj_stack.size()
obj_stack.is_empty()
