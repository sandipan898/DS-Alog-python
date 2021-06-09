# 1. Calculating Average using traditional method
print("1. Calculating Average using traditional method")
total = 0
count = 0
while True:
    inp = input("Enter a Number: ")
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count += 1
average = total / count
print("Average of the numbers is:", average)

# 2. Calculating Average using list method
print("2. Calculating Average using list method")
numbers = list()
while True:
    inp = input("Enter a Number: ")
    if inp == 'done': break
    value = float(inp)
    numbers.append(value)
average = sum(numbers) / len(numbers)
print("Average of the numbers is:", average)

