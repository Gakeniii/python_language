#!/usr/bin/python
#################################
#      Arithmetic progression
#      Name : Sifa Gakeni
#      Date : 26 / 05 /2022
##################################

#First n terms of AP
#a = first_number
#d = steps(common_difference)
#n = number_of_terms

a = int(input("enter the number"))
d = int(input("enter the number"))
n = int(input("enter the number"))
for i in range(1, n + 1):
    n_term = a + (i - 1)*d
    print(n_term) 

#sum of nth term
sum_n = (n/2) * (2*a + (n-1)*d)
print(f"sum of number : {sum_n}")

#Geometric progression
a = int(input("enter the number"))
r = int(input("enter the number"))
n = int(input("enter the number"))
for i in range(1, n + 1):
    n_t = a * r**(i-1)
    print(n_t)

a = int(input("enter the number"))
r = int(input("enter the number"))
n = int(input("enter the number"))

if(r>1):
    sum_n = (a*(r**n))/(r-1)
else:
    sum_n = (a*(r**n))/(1-r)
print("Sum of n terms:" ,sum_n)
    
