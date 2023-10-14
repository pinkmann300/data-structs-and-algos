class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# The above definition of a linked list is a very inductive definition. 

# Define a function to print out all the elements of a ListNode. 


def display(llist):
    current = llist
    while current:
        print(current.val)
        current = current.next 

def writeEvenEl(llist):
    l3 = ListNode(-1)
    l4 = l3 
    while llist is not None:
        if ((llist.val) % 2 == 0):
            l4.next = ListNode(llist.val)
            l4 = l4.next 
            llist = llist.next

        else: 
            llist = llist.next

    return l3.next 


def reverseList(llist):
    prev = None 
    current = llist 

    while current is not None:
        temp = current.next 
        current.next = prev
        prev = current 
        current = temp 

    return prev 

        

w1 = ListNode(5, ListNode(6, ListNode(7, ListNode(8, None))))


camavinga = reverseList(w1)
display(camavinga)


