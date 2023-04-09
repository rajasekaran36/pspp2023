'''
13a) Write a Python function to reverses a string if it's length is a multiple of 3.
'''

string = input('Enter string:')
length = len(string)
if length%3==0:
    print(string,'lenth is multiple of three')
    print('reverse of',string,'is',string[::-1])
else:
    print(string,'length is not multiple of three')
