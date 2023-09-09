class Node: #every node has 2 part => 1.store data from variable , 2.store location 
    def __init__(self,item):
        self.item = item 
        self.next = None 

class LinkedList: #initially head is None 
    def __init__(self):
        self.head = None 
    
    #add_end of Nodes:
    def add_end(self,new_item):
        new_node = Node(new_item) #similar llist.head = Node(item)

        if self.head is None:
            self.head = new_node
            return
        
        last_item = self.head #store the first head.item in last_item... then
        while last_item.next: # Travers until get last_item.next.... last_item.next.next.next....
            last_item = last_item.next # Now , last_item => get last item from head ...
        last_item.next = new_node # Now, last_item is the last element and store the new_node

    

llist = LinkedList()

llist.head = Node(2) #***now llist inherites Node class , Now LinkedList(class) get's Node(class) attribute(item,next) | when create Node (2), it's take a space from memory and also get a address which point/reference to head . example => =>  llist.head = Node(2) []
# print(dir(llist.head)) # check the inherites items of Node (classes).

second = Node(4) 
third = Node(5)


llist.head.next = second #second memeory location point to llist.head.next
second.next = third #third memeory location point to llist.head.next.next.item




#*** how item print -----------------------------
print(llist.head.item, end=" ")  #llist.head = Node(2)
print(llist.head.next.item, end=" ") # llist.head.next = second
print(llist.head.next.next.item, end=" \n") #second.next = third 
print(llist.head.next.next.next, end=" <--check  last item of third.next \n") #third is the last element that's why , third.next=None
# print(dir(llist.head)) # check the LinkedList class that inherites Nodes class and get's Node's attributes (item,next).

#add New item in the end 
llist.add_end(8)

#print item with while loop : 
while llist.head is not None: #travers all Nodes until None of llist.head
    print(llist.head.item, end=" ")
    llist.head = llist.head.next #next llist.head will be llist.head.next and continue to travers all head items...


    



