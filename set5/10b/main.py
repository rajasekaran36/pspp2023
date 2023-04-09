'''
10b) Write a Python Program to implement the following Python tuple operation
i) Create a Tuple
ii) Find the length of the Tuple
iii) find the maximum and minimum element in the tuple
'''
N = int(input('Enter no of elements:'))
elements = []
for i in range(1,N+1):
    print('Enter',i,'element:')
    elements.append(int(input()))
tuple_elements = tuple(elements)
print('Tuple:',tuple_elements)
print('Length:',len(tuple_elements))
print('MAX:',max(tuple_elements))
print('MIN:',min(tuple_elements))