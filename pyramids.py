#!/usr/bin/python

#Printing a half-triangle patterns for astericks
rows = int(input("enter the nunber of rows:"))
for i in range(rows) :
    for j in range(i + 1):
        print("*" , end="")
    print("\n")

#Printing a 
rows = int(input("enter the number of rows: "))
k = 0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end=" ")
    while k != (2*i-1):
        print("*" , end=" ")
        k +=1
    k = 0
    print()