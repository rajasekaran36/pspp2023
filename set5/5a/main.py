'''
5a) Write a Python program to Remove the Duplicate Element in the Tuple
'''

a_tuple = (4,5,1,4,5,6,7,8,1,9)
print('Before removing duplicates:',a_tuple)
a_list = list(a_tuple)
for element in a_tuple:
    while(a_list.count(element)>1):
        a_list.remove(element)
a_tuple = tuple(a_list)
print('After removing duplicates:',a_tuple)


