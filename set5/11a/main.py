'''
11a) Write a program to create a menu with the following options
1.ADDITITON OPERATION
2.SUBSTRACTION OPERATION
3.MULTIPICATION OPERATION
4.DIVISION OPERATION
Accepts users input and perform the operation accordingly.
'''
num1 = int(input('Enter number1:'))
num2 = int(input('Enter number2:'))
print('1.Addition\n2.Substraction\n3.Multiplication\n4.Division')
choice = int(input('Enter choice:'))

if choice==1:
    result = num1 + num2
    print('addition result:',result)
elif choice==2:
    result = num1 - num2
    print('substraction result:',result)
elif choice==3:
    result = num1 * num2
    print('multiplication result:',result)
if choice==4:
    result = num1 / num2
    print('division result:',result)