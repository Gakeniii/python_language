#!/usr/bin/python

#################################
#      Quadratic equations
#      Name : Sifa Gakeni
#      Date : 31 / 05 /2022
##################################


import math
a =int(input("Enter the coefficient of the first term"))
b =int(input("Enter the coefficient of the second term"))
c =int(input("Enter the constant"))
w = math.sqrt((b**2) - (4*a*c))/(2*a)

def find_roots(a,b,c):
    root_1 = (-b + w)
    root_2 = (-b - w)
print("The roots of the quadratic equation are:", y_1 , y_2)
find_roots(a,b,c)


