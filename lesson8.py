#!/usr/bin/python

#tabs \t
print("Monday\tTuesday\tWednesday\tThursday\tFriday\t")
#newline \n
print("Kisumu\nNairobi\nMombasa\n")
#!/usr/bin/python

#################################

#      Dictionaries
#      Name : Sifa Lookia
#      Date : 23/ 09 /2003 
##################################


# Initializing dictionaries
student = {"Name" : "Sifa" , "age" : 18 , "gender" : "female" , "hobbie" : "reading"}
print(student["Name"])
print(student["age"])
print(student["gender"])
print(student["hobbie"])
student ["ID-No"] = "40751481"
student ["Club"] = "Man-city"
print(student)

#Starting with an empty dictionary

student = {}
student["fav-food"] = "chapati"
student["home_city"] = "Nairobi"
student["fav_song"] = "No_wahala"
print(student)

#Modifying the values in a dictionary
student["Name"] = "Athelia"
student["age"] = 21
print(student)

#Removing key values from a dictionary
del student["fav-food"]
print(student)


#Returning  dictionary from a function
def create_full_name(first_name,second_name):
    person = {'first':first_name, 'second':second_name}
    return person
print(create_full_name("Sifa","Gakeni"))
