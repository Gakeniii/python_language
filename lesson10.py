#!/usr/bin/python


#What are dictionaries
#dictionaries is a collection of value pairs

#Syntax: dictionaries = {'key':'value'}
colour= {'colour':'red'}
vehicle= {'type':'toyota' ,'plate_number':'KYZ45'}
#print(type(name)) # we use this method to read the data type of a string
#Accessing values in a dictionary
print(vehicle['type']) #You can access the value of an element inside a dictionary using the key
print(vehicle['plate_number'])
print(vehicle)

#dictionary of a person
person= {'name':'Athelia lutomia' , 'address':'lavington' , 'number':'+254717003992'}
person['age']='21'
print(person['name'])
print(person['address'])
print(person['number'])
print(person)
del person ['number']
print(person)
person= {'Name','Athelia lutomia' 
         'Address','lavington' 
         'Number','+254717003992'}

#Loop in over in dictionaries
#for key, value in person.items():
#        print(f"{value}:{key}")


#Using get to access the value in a dictionary
print(person.get["location', 'the 'location'is non existence"])


#####################################################################

mary_fav_food = ['beef','chicken','vegetable']
jane_fav_food = ['rice','ugali','potatoe']






