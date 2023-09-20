
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

def fib(n: int) -> int:
        arr = [0,1]
        if (n == (0 or 1)):
            return arr[n] 
        else:
            for i in range(2,n+1):
                fibnum = arr[len(arr)-1] + arr[len(arr)-2]
                arr.append(fibnum)

            return arr[n]
        

            

