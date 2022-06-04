#!/usr/bin/python
#################################
#      Classes
#      Name : Sifa Gakeni
#      Date : 02 / 06 /2022
##################################


#create a class that will have employee name and salary
class employee:
    def __init__ (self, _name, _salary, _ID):
        self.name=_name
        self.salary=_salary
        self.ID=_ID

    def sayHi(self):
        print("Hello my name is" + self.name,"my salary is" + self.salary, "and my employees ID is" + self.ID)

employee1 = employee("Soila",str(1700000),str(1230009))
employee1.sayHi()
    
