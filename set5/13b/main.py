'''
13b) Write a Python Program to count the number of Words present in a text file.
'''

file = open('input.txt','r')
data = file.read()
words = data.split()
print('The File Content:')
print(data)
print("No of words:",len(words))
file.close()
