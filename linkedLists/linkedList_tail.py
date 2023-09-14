#!/usr/bin/python3

#The below code is a small amendment from the previous implementation of 
#linked lists in the sense that this has a tail pointer also attached to the same. 

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 


    #Function name: isEmpty
    #Output: Returns if the linked list doesn't have any elements.
    #Complexity: O(1)
    def isEmpty(self):
        return (self.head is None) and (self.tail is None)
    

    #Function name: pushFront 
    #Output: Returns a list with the parameter value added at the beginning of the list.
    #Complexity: O(1)
    def pushFront(self,data):
        newNode = Node(data,None)
        if self.isEmpty():
            self.head = newNode 
            self.tail = newNode
        else:
            temp = self.head 
            newNode.next = temp 
            self.head = newNode 


    #Function name : topFront 
    #Output : Value of top element of the list
    #Complexity :  O(1)
    def topFront(self):  
        return (self.head.data)
    

    #Function name: popFront 
    #Output : Returns a linked list with the first element removed.
    #Complexity: O(1)
    def popFront(self):
        if (self.tail == self.head) and (not self.isEmpty()):
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
        return self


    #Function name: pushBack 
    #Output: Returns the linked list with the parameter value added as a node at the back of the linked list.
    #Complexity: O(1)
    def pushBack(self, key):
        newNode = Node(key,None)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            last = self.tail 
            last.next = newNode
            self.tail = newNode
        return 
    

    #Function name: popBack 
    #Output: Returns a linked list with the last element removed.
    #Complexity: O(n)
    def popBack(self):
        if self.isEmpty():
            return self
        else:
            if (self.head == self.tail) and (not self.isEmpty()):
                self.tail = None
                self.head = None
            else:
                current = self.head 
                while current.next.next is not None:
                    current = current.next
                current.next = None
                self.tail = current
        
        return self

    #Function name: TopBack 
    #Output: Returns the value of the last node in the linked list.
    #Complexity: O(n)
    def topBack(self):
        if self.isEmpty():
            return None 
        else: 
            return self.tail.data 
        
   
    #Function name: display
    #Output: displays the linked list with its values. 
    #Complexity: O(n)
    def display(self):	
        current = self.head 
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    

    #Function name: FindKey 
    #Output: Returns true if the value is found
    #Complexity: O(n)
    def findKey(self, key):
        found = False
        if self.isEmpty():
            return False 
        else:
            current = self.head 
            while current is not None:
                if (current.data == key):
                    found = True 
                    break 
                else:
                    current = current.next
        return found
    
      
    #Function name: addAfter
    #Output: Adds a node with nkey value after the node with data value of key
    #Complexity: O(n)
    def addAfter(self,key,nkey):
        if (not self.isEmpty()) and (self.findKey(key)):
            current = self.head 
            newKey = Node(nkey, None)
            while current is not None:
                if (current.data == key):
                    temp = current.next 
                    newKey.next = temp 
                    current.next = newKey
                    break 
                else:
                    current = current.next
        else:
            print("LinkedList doesn't contain ", key," value entered.")


    #Function name : addBefore 
    #Output: Adds a node before the given key value with the nkey value 
    #Complexity: O(n)
    def addBefore(self,key,nkey):
        if (not self.isEmpty()) and (self.findKey(key)):
            newKey = Node(nkey,None)
            if self.head.data == key:
                temp = self.head 
                newKey.next = temp 
                self.head = newKey
                return 
            else:
                current = self.head 
                while current is not None:
                    if (current.next.data == key):
                        temp = current.next 
                        newKey.next = temp 
                        current.next = newKey
                        break 
                    else:
                        current = current.next 
        else:
            print("Nope not happening")




# Main Program begins here 
l3 = LinkedList()
l3.pushFront("Sunday")
l3.popBack()


