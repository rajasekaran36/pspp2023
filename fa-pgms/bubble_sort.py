numbers = [9,8,1,7,3,4,5]
print('before sort:',numbers)
for i in range(len(numbers),0,-1):
    for j in range(i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    print(numbers)
print('after sort:',numbers)