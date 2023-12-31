
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

def validParen(s):
    eSt = Stack()

    for i in range(0,len(s)):
        if s[i] in ['(', '[']:
            eSt.pushKey(s[i])
        else:
            if eSt.isEmpty():
                return False 
            else:
                top = eSt.topStack()
                eSt.popStack()
                if (top == '[' and s[i] != ']') or (top == '(' and s[i] !=  ')'):
                    return False
    
    return eSt.isEmpty()

"""
The above is an example of implementation of a stack with an array. 
Stacks can be implemented using other data structures such as linkedLists. 

They form a LIFO - Last in First out system. 

Linked list implementation of stacks are more commonly prefered over the 
array implementations in C++ because arrays are a fixed size data structure in C++.


Each stack operation is O(1) : Push, Pop, Top, Empty
"""


