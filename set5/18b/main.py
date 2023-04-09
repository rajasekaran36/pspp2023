'''
18b) Write a Python program to find the longest words in a file.
'''
file = open('input.txt','r')
file_data = file.read()
print(file_data)
words = file_data.split()
long_Word = words[0]
for word in words:
    if(len(long_Word)<len(word)):
        long_Word = word
print("Longest Word is:",long_Word)