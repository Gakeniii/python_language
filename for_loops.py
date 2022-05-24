#!/usr/bin/python


#################################

#      Loops : for loop
#      Name : Sifa Lookia
#      Date : 23/ 09 /2003 
##################################

from traceback import print_tb
from typing import Pattern


print("number\tsquare")
print("==============")
for number in range(0,9):
    print(number)
    print("\t")
    print(number**2)
    
#print a pyramid of stars 
rows = int(input("Enter the number of rows:"))

for i in range(rows):
    for j in range(i+1):
        print("*" , end="")
    print("\n")

rows = int(input("Enter the number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end=" ")

    while k!=(2*i-1):
        print("*", end="*")
        k += 1

    k = 0
    print()    

  


