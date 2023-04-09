'''
16a) Write a Python program to append text to a file and display the text in the output screen.
'''
file = open('input.txt','a+')
string = input('Enter content to append:')
file.write(string)
file.seek(0)
file_data = file.read()
print("File Data")
print(file_data)
