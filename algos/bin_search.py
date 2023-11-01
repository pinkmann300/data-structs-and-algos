"""
The below is an implementation of the binary search in python. The binary search is used to return the index value of a particular element in a sorted array. 
We repeatedly check the middle element of an array and get rid of one half of the array in order to 
"""

def binary_search(arr,val):
    l = 0 
    r = len(arr) - 1 
    while l <= r:
        m = (l + r) // 2
        if arr[m] == val and ((arr[m - 1] != val) or m == 0):
            return m 
            break 
        else:
            if (arr[m] >= val) or (arr[m - 1] == val):
                r = m - 1
            else:
                l = m + 1
    
    return -1 


#Main program begins here 

arr1 = [2,2,3,3,3,3,3,3,32]
ind_val = binary_search(arr1,3)

print(ind_val)


 


