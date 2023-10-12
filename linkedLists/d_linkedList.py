"""
The below is an implementation of the doubly linked lists in Python 

A doubly linked list is an improvement on the singly linked list data structure 
because the running time for some common functions like PopBack become a constant 
time (O(1) in Big-O notation) operation.


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
                else:
                    current = current.next 
        
        return found 
    


# Main program begins here  

l3 = dLinkedList()
l3.pushBack("Monday")

l3.pushBack("Tuesday")
l3.pushBack("Wednesday")
l3.pushBack("Thursday")
l3.pushBack("Friday")

l3.popBack()

print(l3.topBack())

l3.display()


