"""
Two nested for loop.
Time Complexity: O(n^2)
"""

def for_loop_multiply(n, m):
    for i in range(1, n):
        for j in range(1, m):
            print(i, j)
         
for_loop_multiply(3, 4)