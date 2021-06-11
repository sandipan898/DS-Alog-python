first_tuple = (1, 3, 5, 7, 9)
second_tuple = (2, 4, 6, 8)

# 1. Concatenation
concatenation = first_tuple + second_tuple
print("Concatenation:", concatenation)

# 2. Multiplication
multiple = second_tuple * 3
print("Multiplication:", multiple)

# 3. in Operator
print("in Operator:", 4 in multiple)

# 4. count method
print("Count method:", multiple.count(2))

# 5. index method
print("Count method:", multiple.index(2))

# 5. len() method
print("len() method:", len(multiple))

# 5. max() method
print("max() method:", max(multiple))

# 6. min() method
print("min() method:", min(multiple))

# 7. tuple() method
print("tuple() method:", tuple([1,2,3,5,7,0]))
