'''
6)b)Write a Python program to create a dictionary from a string and count the letters from the
string. 
Sample string : 'ENGINEERING'
Expected output: {'E': 3, 'N': 3, 'G': 2, 'I': 2, 'R': 1}
'''

string = input("Enter a string:")
count_dict = {}

for char in string:
    if char not in count_dict:
        count_dict[char] = string.count(char)

print(count_dict)
