# Python program to
# demonstrate implementation of
# queue using queue module


# from queue import Queue

# # Initializing a queue
# q = Queue(maxsize = 3)

# # qsize() give the maxsize
# # of the Queue
# print(q.qsize())

# # Adding of element to queue
# q.put('a')
# q.put('b')
# q.put('c')

# # Return Boolean for Full
# # Queue
# print("\nFull: ", q.full())

# # Removing element from queue
# print("\nElements dequeued from the queue")
# print(q.get())
# print(q.get())
# print(q.get())

# # Return Boolean for Empty
# # Queue
# print("\nEmpty: ", q.empty())

# q.put(1)
# print("\nEmpty: ", q.empty())
# print("Full: ", q.full())

# # This would result into Infinite
# # Loop as the Queue is empty.
# # print(q.get())
# # -------------------------------------------------output---------------------------------------

# # 0

# # Full:  True

# # Elements dequeued from the queue
# # a
# # b
# # c

# # Empty:  True

# # Empty:  False
# # Full:  False


# # ------------------------------------------------------------------------------------------------
# # pip install queue-implementation
# # ------------------------------------------------------------------------------------------------
# # from queue_linkedlist import Queue

# # # Create a queue
# # q = Queue()

# # # Enqueue elements
# # q.enqueue(1)
# # q.enqueue(2)
# # q.enqueue(3)

# # # Dequeue elements
# # print(q.dequeue())  # Output: 1
# # print(q.dequeue())  # Output: 2
# # print(q.dequeue())  # Output: 3
# # --------------------------------------------------------------------------------------------------
# # Queue implementation in Python

# class Queue:

#     def __init__(self):
#         self.queue = []

#     # Add an element
#     def enqueue(self, item):
#         self.queue.append(item)

#     # Remove an element
#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         return self.queue.pop(0)

#     # Display  the queue
#     def display(self):
#         print(self.queue)

#     def size(self):
#         return len(self.queue)


# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)

# q.display()

# q.dequeue()

# print("After removing an element")
# q.display()

# --------------------------------------------------------------------------------------------------
# from queue import Queue

# q = Queue(maxsize=3)
# q.put(1)
# q.put(2)
# q.put(3)

# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())


# print('Full=>',q.full())
# print('Empty=>',q.empty())