#!/usr/bin/python


#################################

#      Functions
#      Name : Sifa Lookia
#      Date : 31/ 05 /2022 
##################################

#Defining a function

def say_hello():
    print("Hello from JKUAT")
    x = 5
    y = 8
    z = x + y
    print(z)

#calling functions
say_hello()

def bark():
    print("Dogs bark woof woof")
bark()
def cat():
    print("Cats meow")
cat()
def cow():
    print("Cows moo")
cow()

#Function parameters
#A function to add two numbers
def add_numbers(x,y): #the function takes the parameters (xand y)
    sum_numbers = x+y
    print("The sum of the numbers:", sum_numbers)
add_numbers(40,50)
add_numbers(100,309)
add_numbers(6,3)

#A function to multiply two numbers
def product_numbers(x,y):
    product = x*y
    print("The product of the numbers is:", product)
product_numbers(4,9)
product_numbers(23,87)
product_numbers(95,83)

#Using default parameter in a function
def print_name ( name = "Sifa Gakeni"):
    print(name)
print_name("Joseph")

#How to return a function
#Return from a function


#Returning  dictionary from a function
def create_full_name(first_name,second_name):
    person = {'first':first_name, 'second':second_name}
    return person
print(create_full_name("Sifa","Gakeni"))

#write a function that gets the square of numbers
def powers(num,power):
    power_num = num**power
    return power_num
print(powers(6,4))

def get_full_name(f_name,s_name):
    full_name = f_name+ " " + s_name
    return full_name.title()
print(get_full_name("Sifa","Gakeni"))

#Returning  dictionary from a function
def create_full_name(first_name,second_name):
    person = {'first':first_name, 'second':second_name}
    return person
print(create_full_name("Sifa","Gakeni"))

#Parsing a list in a function
def greet_friends(names):
    for name in names:
        msg = "Hello" + name.title() + "!"
        print(msg)
friends =[ 'Kamau' , 'Marx' , 'Nene' , 'Kameshi' , 'Dubs']
greet_friends(friends)