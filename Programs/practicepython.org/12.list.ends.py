# Write a program that takes a list of numbers (for example, 
# a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last 
# elements of the given list.

numbers = [5, 10, 15, 20, 25]
print(numbers[0], numbers[-1] if len(numbers)>1 else '')