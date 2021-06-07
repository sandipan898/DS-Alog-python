from array import *

# 1. Create an array and traverse    
print("STEP: 1")       
my_array = array('i', [1, 2, 3, 4, 5])
for i in my_array:
    print(i)

# 2. Access Individual elements through indices
print("STEP: 2")       
print("At Index 0:", my_array[0])
print("At Index 3:", my_array[3])

for i in range(len(my_array)):
    print(my_array[i])

# 3. Append any value to the array using append() method
print("STEP: 3")       
my_array.append(7)
print(my_array)

# 4. Insert value in an arrar using insert() method
print("STEP: 4")       
my_array.insert(0, 0)
my_array.insert(len(my_array), my_array[len(my_array)-1] + 1)
print(my_array)

# 5. Extend python array using extend() method
print("STEP: 5")       
another_array = array('i', [10, 11, 24])
my_array.extend(another_array)
print(my_array)

# 6. Add items from the list into array using fromlist() method
print("STEP: 6")       
sample_list = [20, 21, 22, 23, 24]
my_array.fromlist(sample_list)
print(my_array)

# 7. Remove any array element using remove method (remove the first occurance of the element)
print("STEP: 7")       
my_array.remove(24)
print(my_array)

# 8. Remove last array element using pop() method
print("STEP: 8")       
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method
print("STEP: 9")       
print("Index of {} is {}".format(21, my_array.index(21)))

# 10. Using reverse() method to reverse an python array
print("STEP: 10")       
