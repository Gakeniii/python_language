#!/usr/bin/python
#################################
#      File : Operations
#      Name : Sifa Gakeni
#      Date : 06 / 06 /2022
##################################



def add_numbers(x,y):
    sum = x + y
    return sum

def multiply_numbers(x,y):
    product = x*y
    return product

def sub_numbers(x,y):
    subtract = x-y
    return subtract

def div_numbers(x,y):
    division = x/y
    return division
    

class student:
    def __init__(self,name,hobby,year_of_birth):
        self.name = name
        self.hobby = hobby
        self.year_of_birth = year_of_birth

def greet_student(name):
    print("Hello from student")
