"""
    The below is an implementation of queues in the Python programming language. Queues are an abstract data type which has the following operations defined on them:
        1) Enqueue (Key a) : Appends the key a to the end of the queue
        2) Dequeue() : Removes the element at the front of the queue. 
        3) Empty? : Returns a boolean value of True if the queue is empty and False otherwise.

    Queues are an example of a FIFO data structure. (First In First Out).
"""


class Node:
    def __init__(self,data,next,prev):
        self.data = data 
        self.prev = prev
        self.next = next


class dLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def isEmpty(self):
        return (self.tail is None) 
    
    def pushFront(self,data):
        newNode = Node(data,None,None)
        if self.isEmpty():
            self.head = newNode 
            self.tail = newNode 
        else:
            temp = self.head 
            newNode.next = temp 
            newNode.prev = None
            self.head = newNode
        
    
    def topFront(self):
        return (self.head.data)
    

    def popFront(self):
        self.head = self.head.next
        self.tail = self.tail.prev 


    def pushBack(self, key):
        newNode = Node(key,None,None)
        if self.isEmpty():
            self.pushFront(key)
        else: 
            temp = self.tail 
            temp.next = newNode 
            newNode.prev = temp 
            newNode.next = None
            self.tail = newNode
        return 
    

        
    def popBack(self):
        if self.isEmpty():
            raise Exception("LinkedList has no elements to pop!")
        else:
            temp = self.tail 
            temp.prev.next = None 
            self.tail = temp.prev 

        return 


    
    def topBack(self):
        return (self.tail.data)
    
    def display(self):
        current = self.head 
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    

    def findKey(self, key):
        found = False 
        if self.isEmpty():
            return False 
        else:
            current = self.head 
            while current:
                if current.data == key:
                    found = True 
                    return current
                else:
                    current = current.next 

        if found == False:
            raise Exception("Element not found in the linkedList")


    def addBefore(self,key,nkey):
        nodeInQue = self.findKey(key)
        if (self.head == nodeInQue) and (self.tail == nodeInQue):
            self.pushFront(nkey)
        elif (self.head == nodeInQue):
            newNode = Node(nkey,None,None)
            newNode.next = nodeInQue
            self.head = newNode
        else:
            newNode = Node(nkey,None, None)
            temp = nodeInQue.prev
            newNode.prev = temp 
            newNode.next = nodeInQue
            temp.next = newNode
        
        return 
    
    def addAfter(self,key,nkey):
        nodeInQue = self.findKey(key)
        if (self.head == nodeInQue) and (self.tail == nodeInQue):
            self.pushBack(nkey)
        elif (self.tail == nodeInQue):
            self.pushBack(nkey)
        else:
            newNode = Node(nkey, None, None)
            temp = nodeInQue.next 
            newNode.next = temp 
            newNode.prev = nodeInQue
            nodeInQue.next = newNode

        return
    

class Queue:
    def __init__(self):
        self.q = dLinkedList()
        
    def enqueue(self,k):
        self.q.pushBack(k)
        return 

    def dequeue(self):
        self.q.topFront()
        self.q.popFront()
        return 

    def isEmpty(self):
        return (self.q.isEmpty())


#Main program begins here 

q1 = Queue()

q1.enqueue("Sunday")
q1.enqueue("Monday")
q1.enqueue("Tuesday")
q1.enqueue("Wednesday")

q1.q.display()
q1.dequeue()

print("Performing one action of dequeue: ")
q1.q.display()