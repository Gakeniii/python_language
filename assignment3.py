#!/usr/bin/python


#Write a programme that gets user input and add 10000 to her account if she is between 25-30 years

age = input("What is your age?")
gender = input("What is your gender: male/female")
acc_bal = 0

if (int(age) > 25) and (int(age) < 30):
    acc_bal =  acc_bal + 10000
    print("Confirm you have received ksh 10000")
else:  
    print("Sorry no money for you")

#Write a program to withdraw ksh25000 if the acc_bal is between ksh100000-
#30% if acc_bal is between ksh50000-1000000
#if above ksh1000000 deduct ksh15000