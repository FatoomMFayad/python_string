num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
num_3 = int(input('Enter third number: '))

numbers = [num_1, num_2, num_3]
numbers.sort()
print(f"The largest number is {numbers[-1]}")