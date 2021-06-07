"""
Finding the Biggest Number in an Array 
Time Complexity = O(n)
"""

def find_biggest_number(sample_array):
    biggest_number = sample_array[0]     # -------------------------------------> O(1)
    for index in range(1, len(sample_array)):    # -----------------------------> O(n)
        if biggest_number < sample_array[index]: # -----------------------------> O(1) 
            biggest_number = sample_array[index] # -----------------------------> O(1)

    print(biggest_number) # ----------------------------------------------------> )(1)

find_biggest_number([1, 2, 4, 6, 10, 11, 32, 24, 30, 28, 18, 7])


