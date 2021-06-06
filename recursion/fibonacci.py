"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
"""

def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number should be an Positive Integer number"
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(-1))

# for i in range(0, 21):
#     print(fibonacci(i))
