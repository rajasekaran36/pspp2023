'''
19a) Write the Python program To compute sin(x) using the below given Formula
sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........
'''
def factorial(number):
    result = 1
    for i in range(2,number+1):
        result *= i
    return result
    
x = int(input('Enter x value:'))
n = int(input('Enter number of terms:'))
term = 2
positive = False
current = 3
sum = x
while term<=n:
    result = x**current/factorial(current)
    if(not positive):
        result=(-1)*result
        positive = True
    else:
        positive = False
    sum += result
    current+=2
    term+=1
print("sin",x,sum)