# 1. Concatenation with '+'
print("1. Concatenation with '+'")
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# 2. Repeat elements with '*'
print("2. Repeat elements with '*'")
list4 = list1 *3
print(list4)

# 3. len() method
print("3. len() method")
print("length of {} is {}".format(list4, len(list1)))

# 4. max() method
print("4. max() method")
print("Maximum element of {} is {}".format(list3, max(list3)))

# 5. min() method
print("5. min() method")
print("Minimum element of {} is {}".format(list3, min(list3)))

# 6. sum() method
print("6. sum() method")
print("Sum of the elements of {} is {}".format(list3, sum(list3)))

# 7. Calculating Average
print("7. Calculating Average")
print("Average of the elements of {} is {}".format(list3, sum(list3)/len(list3)))
