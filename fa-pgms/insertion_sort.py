numbers = [9,8,1,7,3,4,5]
print('before sort:',numbers)
for i in range(len(numbers),0,-1):
    element = numbers[i]
    for j in range(i,0,-1):
        if numbers[j-1] > element:
            numbers[j],numbers[j-1] = numbers[j-1],numbers[j]
        else:
            numbers[j] = element
    print(numbers)
print('after sort:',numbers)