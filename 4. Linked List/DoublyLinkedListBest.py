"""
doubly linked list Node => has 2 pointer => 1. previous(node) 2. next(node) , 
doubly linked list traversal in => forward + backward position.
"""



class Node: #every node has 2 part => 1.store data from variable , 2.store location 
    def __init__(self,item):
        self.item = item 
        self.next = None 
        self.prev = None

class LinkedList: #initially head is None 
    def __init__(self):
        self.head = None 
        
        
    def forward_traversal(self):
        if self.head == None: 
            print("Linked List is empty!")
            return
        
        a = self.head
        while a is not None: 
            print(a.item, end=" ")
            a = a.next
            
            
    def backward_traversal(self):
        print()
        if self.head == None: 
            print("Linked List is empty!")
            return
        
        a = self.head
        while a.next is not None: 
            a = a.next 
            
        while a is not None:
            print(a.item, end=" ")
            a = a.prev
    
    
n1 = Node(1)

dll = LinkedList()

dll.head = n1 
n2= Node(2)
n2.prev=n1
n1.next=n2 

n3 = Node(3)
n2.next = n3
n3.prev = n2 

n4 = Node(4)
n3.next = n4
n4.prev = n3


dll.forward_traversal()
dll.backward_traversal()









    


