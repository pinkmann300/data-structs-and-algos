
"""
Stacks are an abstract data type with the following operations:

Push(Key) : adds key to collection 
Key Top() : returns most recently added key
Key Pop() : removes ad returns most recently added key. 
Boolean Empty() : Returns whether the stack is empty or not 

"""

class Stack:
    def __init__(self,st=[]):
        self.st = st

    def pushKey(self,key):
        self.st.insert(0,key)
        return 

    def popStack(self):
        self.st = self.st[1:]
        return

    def topStack(self):
        return self.st[0]
    
    def isEmpty(self):
        return (self.st == [])
    


# Main program begins here 

