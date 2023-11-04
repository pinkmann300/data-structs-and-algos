"""
    The below is an implementation of queues using arrays. In order to keep Dequeue as an O(1) operation, we make sure that the 
    array is a circular array and there is no room for you to mess around with the existing space
"""

class Queue:
    def __init__(self,n):
        self.cir_queue = [] 
        self.read = 0 
        self.write = 0

    def isEmpty(self):
        return (self.read == self.write)

    def enqueue(self,key):
        self.cir_queue.insert(write, key)
        self.write += 1 
       
    def dequeue(self):
        print(self.cir_queue[read])
        self.cir_queue[read] = None
        self.read += 1 