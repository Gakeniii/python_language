#!/usr/bin/python

#Write a program to withdraw ksh25000 if the acc_bal is between ksh100000-200000 , 30% to be deducted for acc_bal ksh500000 - ksh 1M, for acc_bal above 1M ksh 15000 is deducted

acc_bal = int(input("Enter you acc_bal"))

if (int(acc_bal) > 100000 and int(acc_bal) < 200000):
    acc_bal = acc_bal - 25000
    print("ksh 25000 has been deducted from your account")
if (int(acc_bal) > 500000 and int(acc_bal) < 1000000):
    acc_bal = acc_bal - (0.3*acc_bal)
    print("We have deducted 30% from your account")
if int(acc_bal)>1000000:
    acc_bal = acc_bal - 15000
    print("ksh 15000 has been deducted from your account")
