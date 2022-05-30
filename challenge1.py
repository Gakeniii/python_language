#!/usr/bin/python

#################################
#      Challenges1
#      Name : Sifa Gakeni
#      Date : 30 / 05 /2022
##################################



#CHALLENGE 1
#write a program to check if a number is divisible by 5 or 7
number = int(input("Enter the number")) 
if (number%7 == 0) and (number%5 == 0):
    print(number,"The number is divible by 7 or 5")
else :
    print( number,"The number is not divisible by 7 or 5")
