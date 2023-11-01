"""
The below is an implementation of the linear search algorithm. The linear search algorithm is an example of an O(n) time complexity algorithm. 
The idea behind the linear search is that given an array and a key value, starting from the first element in the array, you traverse the array one by 
one until you either reach the end of the array or you reach the element itself. In the event you reach the element, you return the index value at which 
the value is held. 
"""

def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i 
            break
        else:
            continue 
    
    return -1

# Main program begins here 

arr1 = [2,3,4,5,6,7,8,8,8,9,9,9,110]
ind_val = linear_search(arr1,110)

print(ind_val)