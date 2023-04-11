'''
19a) Write the Python program To compute sin(x) using the below given Formula
sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........
'''
def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial(number-1)

def exponent(x,p):
    return x**p
    
x = int(input('Enter x value:'))
n = int(input('Enter number of terms:'))
positive = True
sum = 0
for i in range(1,n*2,2):
    if positive:
        sum = sum + (exponent(x,i)/factorial(i))
        positive = False
    else:
        sum = sum - (exponent(x,i)/factorial(i))
        positive = True
print("SIN",x,"value is:",sum)