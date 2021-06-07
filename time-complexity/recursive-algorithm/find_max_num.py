"""
Finding the Biggest Number in an Array 
Time Complexity = O(n)
"""

def find_man_num_rec(array, n): # ------------------------------> T(n)
    if n == 1:                  # ------------------------------> O(1)
        return array[0]         # ------------------------------> O(1)
    return max(array[n-1], find_man_num_rec(array, n-1)) #------> T(n-1)

# resulting in: T(n) = O(1) + T(n-1)
# T(1) = 1
# T(n-1) = O(1) + T(n-2) = 1 + T(n-2)
# T(n-2) = O(1) + T(n-3) = 1 + T(n-3)
# ...
# so T(n) = 1 + T(n-1) 
#         = 1 + 1 + T(n-2) = 2 + T(n-2)
#         = 2 + 1 + T(n-3) = 3 + T(n-3)
#         = 3 + 1 + T(n-4) = 4 + T(n-4)
#         ...
#         = n - 1 + T(n-(n-1))
#         = n - 1 + T(1) =
#         = O(n)

array = [1, 2, 3, 4, 5, 9, 7, 10, 15, 14, 12, 13, 8]
print(find_man_num_rec(array, len(array)))