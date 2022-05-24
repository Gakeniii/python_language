#!/usr/bin/python
#################################
#For lops with lists
#      Name : Sifa Lookia
#      Date : 24 / 05 /2022
##################################

squares = []#empty list
for numbers in range (0, 10):
    square = numbers**2
    squares.append(square)

print(squares)

cubes = []
for numbers in range (0,11):
    cube = numbers**3
    cubes.append(cube)
 
print(cubes)

sum = 0
for numbers in range (0,10):
    sum = sum + numbers

print(sum)

#######################
#if statements

age = 24
if age >= 18:
    print("You are allowed to drive")
else:
    print("You are too young to drive")


#Write a programme that gets user input and add 10000 to her account if she is between 25-30 years
