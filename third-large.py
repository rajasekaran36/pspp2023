def maximum(numbers,limit=9999999999):
    max = numbers[0]
    for number in numbers:
        if max < number and number < limit:
            max = number
    return max

numbers = [4,6,1,8,9,3,2,8]
for i in range(1,4):
    if i==1:
        last_max = maximum(numbers)
    else:
        last_max = maximum(numbers,last_max)
    print(i,'max is:',last_max)