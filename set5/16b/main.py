'''
16b) Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them
'''

name = input('Enter first name and last name:')
print('before reverse:',name)
first_name = name.split()[0]
last_name = name.split()[1]
print('reverse:',last_name[::-1],first_name[::-1])