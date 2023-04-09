'''
9a) Write a python program to that accepts length of three sides of a triangle as inputs. The
program should indicate whether or not the triangle is a right angled triangle (use
Pythagorean theorem)
'''

side_a = int(input("Enter side A:"))
side_b = int(input("Enter side B:"))
side_c = int(input("Enter side C:"))
hypotenuse = ((side_a**2)+(side_b**2))**0.5
if side_c==hypotenuse:
    print('It is right angle triangle')
else:
    print('It is not a right angle triangle')