'''
14a) Create three text file such as “source1.txt”,”source2.txt”, in read mode , “target.txt” in write
mode and write a Python Script to copy the content of “source1.txt”,”source2.txt”, and writethe content in “target.txt file”.
'''

source_file_1 = open('source1.txt','r')
print('Source File 1 Opened')
source_file_2 = open('source2.txt','r')
print('Source File 2 Opened')
target_file = open('target.txt','w')
print('Target file Opened')
data_from_file_1 = source_file_1.read()
print('Source File 1 Read Completed')
data_from_file_2 = source_file_2.read()
print('Source File 2 Read Completed')
target_file.write(data_from_file_1)
print('Target Written with Source File 1 Content')
target_file.write(data_from_file_2)
print('Target Written with Source File 2 Content')
source_file_1.close()
print('Source File 1 Closed')
source_file_2.close()
print('Source File 2 Closed')
target_file.close()
print('Target File Closed')