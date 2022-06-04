 #vehicle class should have mileage speed and distance
class vehicles:
    def __init__(self, _max_speed, _mileage):
        self.max_speed = _max_speed
        self.mileage = _mileage
Toyota = vehicles(str('300km/h'),str(200))
print("Toyota mileage is " + Toyota.mileage + "and maximum speed is" + Toyota.max_speed)

Mercedes =vehicles(str(200),str(50))
print("The Mercedes milage " + Mercedes.mileage + "and milage " + Mercedes.max_speed)  


