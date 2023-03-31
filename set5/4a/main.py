'''
Write a Python program that prints out the decimal equivalents 
of 1/2, 1/3, 1/4, . . . ,Using for loop
'''

limit = int(input('Enter limit:'))
for i in range(2,limit+1):
    print(1,'/',i,'=',1/i)
