my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}

# 1. in operator
print("Using in operator")
print("for Key,", 'one' in my_dict) # ----------------> O(1)
print("for Value,", 1 in my_dict.values())

# 2. for operator
print("Using for operator") # ---------------> O(n)
for key in my_dict:
    print(key, my_dict[key])

# 2. all() method
print("Using all() method") 

sample_dict1 = {0: True, 1: True}
print(all(sample_dict1))

sample_dict2 = {0: False, 1: False}
print(all(sample_dict2))

sample_dict3 = {0: True, 1: False, 2: False}
print(all(sample_dict3))