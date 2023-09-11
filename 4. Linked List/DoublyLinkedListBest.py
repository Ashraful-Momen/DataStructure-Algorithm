"""
doubly linked list Node => has 2 pointer => 1. previous(node) 2. next(node) , 
doubly linked list traversal in => forward + backward position.

*** head actually is used to point address of 1st node /keeping data. but among the all nodes, head actually
out of nodes but  is used to point address of 1st node /keeping data.

ex : None <-prev.head.next->  <-prev.n1.next-> <-prev.n2.next-> <-prev.n3.next->.... <-prev.n.next-> None
---------------------------> Node start from here n1. and head is extra part of Nodes.
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
        while a is not None: #By default a.address is note none... but a.item =print the value of item
            print(a.item, end=" ")
            a = a.next
            
            
    def backward_traversal(self): 
        print()
        if self.head == None: 
            print("Linked List is empty!")
            return
        
        a = self.head
        while a.next is not None: # first we need to go forward to get a.next all value and
            a = a.next 
            
        while a is not None: #By default a.address is not none...
            print(a.item, end=" ")
            a = a.prev
    
    def insert_add_beginning(self, item):  # Corrected method name
        nb = Node(item)
        a = self.head

        if a is not None:
            a.prev = nb  # Set previous of current head to the new node
            
        # a.prev = nb
        nb.next = a  # Set next of new node to current head
        nb.prev = None  # Set previous of new node to None
        self.head = nb  # Set new node as head   
    
    def  insertion_add_end(self,item):
        ne = Node(item) # n.prev = none , n.next = none
        last_item = self.head # last item is a copy of first node.
        
        while last_item.next is not None: #need last_item.next == None , where we add new Node
            last_item = last_item.next # after loop we get last_item == where last.next ==None
        # have to convert (ne) Node to last_item.
        last_item.next = ne # last_item.nxt get address of (ne) 
        ne.prev = last_item #
        ne.next = None
    
    def insertion_add_specific(self,position,item): #
        ns = Node(item)
        a = self.head 
        
        for i in range(1,position-1):
            a= a.next 
        
        # assing new node pointers ns->(prev & next)
        ns.prev=a 
        ns.next=a.next  
        
       # have to fix ns next node pointer = a.next.prev and a.next 
        a.next.prev = ns # that means 3 position node.prev point -> ns (address).
        a.next=ns
        
    def delete_beginning(self):
        a = self.head # point first node
        self.head = a.next #point second node
        a.next = None
        self.head.prev = None
    
    def delete_end(self): # for end delete need 2 variable. 1st varibale will be last node and 2. variable will be previous node of last node 
        a = self.head.next
        before = self.head 
        
        while a.next is not None:
            a = a.next 
            before = before.next
            
        before.next = None 
        a.prev = None 
    
    def delete_specific_position(self,position): # also need 2 variable for delete specific postions.
        before = self.head 
        a = self.head.next 
        
        for i in range(1,position-1):
            a= a.next 
            before = before.next 
            
        before.next = a.next 
        a.prev = before 
        
        a.next = None 
        a.prev = None 
        
    
    
        
    
    
        
        


dll = LinkedList()
n1 = Node(1)

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

dll.insert_add_beginning(0)
# dll.insert_add_beginning(-1)
dll.insertion_add_end(5)
# dll.insertion_add_specific(6,6)  #(position ,item)

# dll.delete_beginning()
# dll.delete_end()
dll.delete_specific_position(6)



dll.forward_traversal()
dll.backward_traversal()









    


