#!/usr/bin/python

#################################
#      Arithmetic progression
#      Name : Sifa Gakeni
#      Date : 27 / 05 /2022
##################################


#calculate the factorial of 6 (method 2)
number = int(input("enter the number"))
factorial = 1
if number < 0:
    print("factorial of negative number does not exist")
elif number == 0:
    print("factorial of 0 = 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f"factorial of number is:{factorial}")


