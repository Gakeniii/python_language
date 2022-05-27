#!/usr/bin/python


for numbers in range(0,10):
    if(numbers %2 == 0):
        print(numbers)

#sum of all even numbers between (0,50)
sum = 0
for number in range(0,50):
    if(number %2 == 0):
        sum = sum + number
print(sum)

#product of odd numbers betweeen (1,10)
product =6
for number in range(0,10):
    if(number %2 == 1): #Odd number
        product = product*number
print(product)

#Calculate the factorial of six (6!)
num = 6
factorial = 1
if num < 0:
    print(factorial)
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
        print("The factorial of", num, "is", factorial)

#calculate the factorial of 6 (method 2)
n = int(input("enter the number"))
factorial = 1
if number < 0:
    print("factorial of negative number does not exist")
elif num == 0:
    print("factorial of 0 = 1")
else:
    for number in range(1, num + 1):
        factorial = factorial * 1
    print(f"factorial of number is:{factorial}")



#while loop
num = 0
while num < 10:
    print(num)
    num = num + 1
    
num = 0
while num < 10:
    if(num %2 == 0):
        print(num)
    num = num + 1

