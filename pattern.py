#!/usr/bin/python

#Programme for printing patterns of numbers
rows = int(input("enter the number of rows"))
for i in range(rows):
    for j in range(i + 1):
        print(j + 1 , end="")
    print("\n")

rows = int(input("enter the number of rows"))
k = 0
