'''
10a) Define a function fact and write a python Script to find the factorial of a number
'''

def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)

number = int(input('Enter number to find factorial:'))
print('Factorial of number',number,'is',factorial(number))
