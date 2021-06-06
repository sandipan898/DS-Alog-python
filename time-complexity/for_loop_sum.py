"""
Two separate for loop.
Time Complexity: O(n)
"""

def for_loop_sum(n, m):
    for i in range(1, n):
        print(i, end=" ")
    
    print()
    for i in range(1, m):
        print(i, end=" ")

for_loop_sum(3, 4)
