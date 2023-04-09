'''
8b) Write a Python program to print the sum of first 100 odd numbers.
'''
count = 0
current = 1
sum = 0
while count<=100:
    if(current%2==0):
        sum +=current
        count +=1
    current+=1
print('Sum of first 100 odd numbers:',sum)
