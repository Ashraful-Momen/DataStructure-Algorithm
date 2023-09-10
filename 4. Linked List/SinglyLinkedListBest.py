# Singly LinkedList : is forward direction , Node=> data, pointer


class Node: #every node has 2 part => 1.store data from variable , 2.store location 
    def __init__(self,item):
        self.item = item 
        self.next = None 

class LinkedList: #initially head is None 
    def __init__(self):
        self.head = None 
        
        
    def traversal(self):
        if self.head == None: 
            print("List is empty!")
            return 
        node = self.head
        while node is not None: 
            print(node.item, end=" ")
            node = node.next 
  
    #insert_add_end of Nodes:
    def insert_add_end(self,new_item):
        new_node = Node(new_item) #similar Slist.head = Node(item)

        if self.head is None:
            self.head = new_node
            return
        
        last_item = self.head #by default self.head indicate the address and self.head.item carry the item value.
        
        while last_item.next is not None: #***don't forget to use last_item.next , either getting non object error for next.
            last_item= last_item.next 
        last_item.next = new_node 
        # print(f'last Last_item check => {last_item}')
    
    #insert add begining: 
    def insert_add_begining(self,item):
        nb = Node(item) # nb.next = none
        nb.next = self.head #head point to fist node , so nb.next = self.head , now nb.next point to first node
        self.head = nb # head and nb bother point first node , now need to head point to nb as first node. 
    
    #insert in specific position:
    def insert_add_position(self,position,item):
        np = Node(item)
        
        a = self.head # store self.head into a , if head delete then whole list will distroy for garbage collection in python.
        
        for i in (range(1,position-1)): #suppose we want to add in position 3 , we need 3 previous position , that's why (position-1)
            a = a.next # update a=head position to previous 3 postion.
        
        np.next = a.next # np.next = None , now np point = 3 postion , which is a.next also .
        a.next = np # now a point to position 2 and np point to position 3. 
    
    #delete begining  
    def delete_begining(self):
        a = self.head 
        self.head = a.next 
        a.next = None  
        
    #delete end:
    def delete_end(self):
        previous = self.head # point to first node
        a = self.head.next # point to 2nd node
        while a.next is not None: #traversal last node
            a = a.next # now a is last node (a is None and loop break / condition false)
            previous = previous.next # previous node is before node of a .
        previous.next = None # previous is before node of a. which is none , so a node is deleted
    
    #delete specific position:
    def delete_specific_position(self,position):
        previous = self.head # 1st position
        a = self.head.next # 2nd position
        for i in range(1,position-1):
            a = a.next # a will be choosen position before node 
            previous = previous.next # previous will be a position's before node.
        
        previous.next = a.next # Now previous and a point the same Node , which we want to  delete
        a.next = None # gone to gerbage collection , deleted.

Slist = LinkedList()


Slist.insert_add_end(1)
Slist.insert_add_end(2)
Slist.insert_add_end(3)
Slist.insert_add_end(4)
Slist.insert_add_end(5)

Slist.insert_add_position(3,9) #(position,item)

# Slist.delete_begining()
# Slist.delete_end()
Slist.delete_specific_position(3) #position 3 , item is 9 .

Slist.traversal()









    


