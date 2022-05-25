#!/usr/bin/python

 
#List of vehicles uisng f statements find a jeep in the list and convert it into uppercase
from multiprocessing import _JoinableQueueType


vehicles = ['bmw', 'jeep' ,'mercedes' , 'toyota' , 'audi']

#using a for loop to print all vehicles
for vehicle in vehicles:
    if vehicle == "jeep":
        print(vehicle.upper())
    else:
        print(vehicles.title())

        
