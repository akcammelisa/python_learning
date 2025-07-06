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

# car1 = Car("Honda", "Blue")
# print(car1)
# car1.drive()     # Honda is now driving at 60 km/h.
# car1.repaint("Black")
# car1.stop()


import threading
import time

# def func1():
#     for x in range(10):
#         print("ONE")

# def func2():
#     for x in range(10):
#         print("TWO")

# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)

# t1.start()
# t2.start()

# x = 1024
# lock = threading.Lock()

# def double():
#     global x, lock
#     lock.acquire()
#     while x < 2048*4:
#         x *= 2
#         time.sleep(1)
#         print(x)
#     print("Reached maximum!")
#     lock.release()

# def halve():
#     global x, lock
#     lock.acquire()
#     while x > 1:
#         x /= 2
#         time.sleep(1)
#         print(x)
#     print("Reached minimum")
#     lock.release()

# t1 = threading.Thread(target = double)
# t2 = threading.Thread(target = halve)

# t1.start()
# t2.start()


# event = threading.Event()

# def myfunction():
#     print("Waiting for the event to trigger...")
#     event.wait()
#     print("Performing action XYZ now...")

# t1 = threading.Thread(target=myfunction)
# t1.start()

# x = input("Do you want to trigger the event? (y/n)")
# if x == "y":
#     event.set()

file = open("text.txt", "w")
file.write("Hello World!")
file.close()

# path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon= True)
t2 = threading.Thread(target = printloop)

t1.start()
t2.start()