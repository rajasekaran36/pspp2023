'''
2. a) Write a Python program to print the below Pyramid
*
**
***
****
*****
'''

for i in range(6):
    for j in range(i):
        print('*',end='')
    print()