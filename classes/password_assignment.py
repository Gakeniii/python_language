#!/usr/bin/python

#################################

#      password generator
#      Name : Sifa Lookia
#      Date : 04/ 06 /2022 
##################################

import random
print("Welcome to your password generator")
num_password = int(input("Enter number of passwords"))
len_passwords = int(input("number of character you would like"))


class passwords:
    def __init__(self,email):
        self.email = email
password1 = passwords(str(input("Enter your email address")))
print("\n Your passwords are here : ")
for passwords in range(num_password):
    password = ''
    for c in range(len_passwords):
        password += random.choice(password1.email)
        print(password)    


