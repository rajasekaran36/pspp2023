'''
4b)Write a Python Program to print the Following number Pattern
55555
4444
333
22
1
'''

for i in range(5,0,-1):
    for j in range(i):
        print(i,end='')
    print()