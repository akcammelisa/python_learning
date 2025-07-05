class Person:
    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return "name:{}, age: {}, height: {}".format(self.name, self.age, self.height)
    
person1 = Person("Layla", 12, 155)
# print(str(person1))
# print(person1)
# person2 = Person("Can", 30, 175)
# print(person2)

print(Person.amount)

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def __str__(self): 
        return "the {} {} is ready! ".format(self.color, self.brand)

    def drive(self):
        self.speed = 60
        print(f"{self.brand} is now driving at {self.speed} km/h.")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} has stopped.")

    def repaint(self, new_color):
        self.color = new_color
        print(f"{self.brand} is now {self.color}.")

car1 = Car("Honda", "Blue")
print(car1)
car1.drive()     # Honda is now driving at 60 km/h.
car1.repaint("Black")
car1.stop()
