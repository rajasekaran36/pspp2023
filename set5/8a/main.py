'''
8a)Write a Python program that accepts a comma separated sequence of words as input and
prints the unique words in sorted form.
input:apple,orange,lemon,papaya,peach,pineapple,watermelon,sapota,mango,papaya,apple,spota,apple,kiwi,muskmelon
'''

input_string = input('Enter comma seprated string:')
words = input_string.split(',')
unique_words = []
for word in words:
    if words.count(word)==1:
        unique_words.append(word)
sorted(unique_words)
for word in unique_words:
    print(word)