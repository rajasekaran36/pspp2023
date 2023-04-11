numbers = [4,2,1,6,7,5,9,8]
print('before sorting:',numbers)
for i in range(len(numbers)-1):
    assumed_min_index = i
    actual_min_index = i
    for j in range(i,len(numbers)):
        if numbers[actual_min_index]>=numbers[j]:
            actual_min_index = j
    if actual_min_index!=assumed_min_index:
        numbers[actual_min_index],numbers[assumed_min_index] = numbers[assumed_min_index],numbers[actual_min_index]
    print(numbers)
print('after  sorting:',numbers)