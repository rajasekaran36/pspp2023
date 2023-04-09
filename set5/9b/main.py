'''
9b) Write a Python Program to Print all Prime numbers less than 50.
'''
print(1)
print(2)
count = 2
current = 3
while count<50:
    prime = True
    for i in range(2,current):
        if(current%i==0):
            prime = False
            break
    if prime:
        print(current)
        count+=1
    current+=1