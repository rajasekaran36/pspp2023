'''
12a)a) Write a Python Program to find the Third Largest number in a given list using Functions
'''
numbers = [2,3,1,4,5,6,7,8,0,8]
print('numbers:',numbers)
for i in range(2):
    maximum = max(numbers)
    while maximum in numbers:
        numbers.remove(maximum)
print("3rd maximum:",max(numbers))