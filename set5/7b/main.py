'''
7b)Write a Python Program to raise ZeroDivisionError if the User enters 0 as numerator or
Denominator value.
'''

numerator = int(input('Enter numerator value:'))
denominator = int(input('Enter denominator value:'))
try:
    if numerator==0 or denominator==0:
        raise ZeroDivisionError
    else:
        result = numerator/denominator
        print('Result:',result)
except ZeroDivisionError:
    print('Exception: numerator or denominator is 0')