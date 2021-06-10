my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}

# 1. in operator
print("Using in operator")
print("for Key,", 'one' in my_dict) # ----------------> O(1)
print("for Value,", 1 in my_dict.values())

# 2. for operator
print("Using for operator") # ---------------> O(n)
for key in my_dict:
    print(key, my_dict[key])

# 2. all() method (Like logical AND)
print("Using all() method") 

sample_dict1 = {0: True, 1: True}
print(all(sample_dict1))

sample_dict2 = {0: False, 1: False}
print(all(sample_dict2))

sample_dict3 = {0: True, 1: False, 2: False}
print(all(sample_dict3))

sample_dict4 = {0: True, 1: True, 2: False}
print(all(sample_dict4))

sample_dict5 = {}
print(all(sample_dict5))

# 2. any() method (Like logical OR)
print("Using any() method") 

sample_dict1 = {0: True, 1: True}
print(any(sample_dict1))

sample_dict2 = {0: False, 1: False}
print(any(sample_dict2))

sample_dict3 = {0: True, 1: False, 2: False}
print(any(sample_dict3))

sample_dict4 = {0: True, 1: True, 2: False}
print(any(sample_dict4))

sample_dict5 = {}
print(any(sample_dict5))

# 3. len() method
print("Using len() method")
print("length of sample_dict4 is", len(sample_dict4))

# 4. sorted() method
print("Using sorted() method")
vowels = {'aaa': 1, 'oo': 2, 'eeeee': 3, 'uuuu': 4, 'iiiiii': 5}
print("Sorted:", sorted(vowels))
print("Sorted in Reverse Order", sorted(vowels, reverse=True))
print("Sorted in terms of Lengths", sorted(vowels, key=len))
