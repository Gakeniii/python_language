#create a programme

#area
radius = input("enter the radius")
pi = 3.142
area = pi * int(radius) * int(radius)

print("The radius of the circle" + (radius))
print("The area of the circle is " + str(area))

#Volume
radius = input("enter the radius")
pi = 3.142
height = input("enter the height")
volume = pi *  int(radius) * int(radius) * int(height)

print("The height of the circle" + (height))
print("The radius of the circle" + (radius))
print("The volume of the cylinder is" + str(volume))

#surface area
radius = input("enter the radius")
pi = 3.142
height = input("enter the height")
x = 2
surfaceArea = pi * 2 * int(radius) * int(radius) * int(height)
print("The height of the circle" + (height))
print("The radius of the circle" + (radius))
print("The surface area of the cylinder is " + str(surfaceArea))

#volume of cube
length = 5
width = 3
height = 15
volume = length * width * height
print("The volume of a cube is" + str(volume))