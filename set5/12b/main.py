'''
12b) Write a Python program to implement the following python List operation
i) Inserting the element at the specified positions
ii)Remove the element in the List
iii)Delete the entire List
iv)Position of the particular Element in a Given List
'''

numbers = [2,3,1,4,5,6,7,8,0]
print('numbers:',numbers)

while (True):
    print('''
    1.Insert an element at position
    2.Remove element in list
    3.Position of particular element
    4.Delete the list
    5.Exit
    ''')
    choice = int(input('Enter your choice:'))
    if choice==1:
        print('before insert:',numbers)
        element = int(input('Enter element to be inserted:'))
        position = int(input('Enter the index position:'))
        numbers.insert(position,element)
        print('after insert:',numbers)
    elif choice==2:
        print('before removal:',numbers)
        element = int(input('Enter element to be removed:'))
        numbers.remove(element)
        print('after removal:',numbers)
    elif choice==3:
        try:
            element = int(input('Enter the element to find the position:'))
            print('Element found at position:',numbers.index(element))
        except ValueError:
            print('Element not found')
    elif choice==4:
        print('before delete:',numbers)
        del numbers
        print('list deleted')
    elif choice==5:
        print('Thank You !!!')
        break
