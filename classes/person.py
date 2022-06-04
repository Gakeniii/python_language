class person:
    def __init__(self, _name, _age):
        self.name= _name
        self.age= _age

    def sayHi(self):
        print('Hello, my name is' + self.name 'and I am' + self.age 'years old')

person1 = person('Malawa' , str(17))
person1.sayHi()

person2 = person('Ally', str(22))
person2.sayHi()

person1 = person('Malawa' , str(17))
person2 = person('Ally', str(22))
person1.sayHi()
person2.sayHi()

student1 = person('Sifa', '007')
print(student1)
