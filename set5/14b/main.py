'''
14b)Write a Python code to get the voters age as input. If the user Enters a Valid age as input
Display the Result otherwise Raise the Exception.
'''

age = int(input("Enter age:"))
try:
    if age >= 18:
        print('You are eligile to vote')
    else:
        raise ValueError
except ValueError:
    print('Exception: You are not elegible to vote')