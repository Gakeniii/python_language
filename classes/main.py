
#!/usr/bin/python
#################################
#      File : Operations
#      Name : Sifa Gakeni
#      Date : 06 / 06 /2022
##################################


import operations
from student import student
from teacher import Teachers
from classes_students import classes

operations.add_numbers(3,5)
operations.sub_numbers(500,88)
operations.multiply_numbers(6,8)
operations.div_numbers(8,2)

print(operations.add_numbers(3,5))
print(operations.sub_numbers(500,88))
print(operations.multiply_numbers(6,8))
print(operations.div_numbers(8,2))


new_student = student("Joan","cycling","1997")
student.greet_student()

new_teacher = Teachers("Mr.John",23253,"Literature",50000)
print(new_teacher.get_tsc_number())

new_class = classes("Form3",50,"West")
print(new_class.get_capacity())