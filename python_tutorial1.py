
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# if x > y:
#     print("x is greater than y")
#     if x>0:
#         print("x is a positive number")
#     else:
#         print("x is a negative number")
   
# elif x < y:
#    print("x is less than y")

#Loops
# x = 0
# while x <10:
#     x +=1
#     print(x)

# for x in range(10):
#     print("Hello World!")

# x = 0
# while x<10:
#     x += 1
#     if x == 5:
#      continue
#     print(x)

# if x == 5:
#    pass

# mylist =[1,2, "dog", 60, True, 9.87]
# print(mylist[:3])

# mylist[3] = "cat"
# print(mylist)

# for x in mylist:
#     print(x)

# mylist2 = [1,2,3,4,5]
# for y in mylist2:
#     print(2**y)

# print(mylist*2)
# print(mylist + mylist2)
# print(max(mylist2))
# print(len(mylist))

# mylist2.append("elephant")
# print(mylist2)

# mylist2.insert(3, "egg")
# print(mylist2)

# mylist2.remove("egg")
# print(mylist2)

# mylist2.pop(3)
# print(mylist2)

# print(mylist2.index("elephant"))

# mylist2.pop(mylist2.index("elephant"))
# print(mylist2)

# a = [23, 1, 5, 99, 4, 65]
# a.sort()
# print(a)
# print(sorted(a))

# #tuples - not changing lists with paranthesis

# y = (1,2,3)
# print(type(y))
# print(y)
# print(y[2])

# y = list(y)
# y[2]= 10
# y = tuple(y)
# print(y)

# #Dictonary = {}, not index but key

# person = {'name': 'Melisa', 'surname': 'Akçam', 'gender': "female"}
# print(person['name'])

# person["newkey"] = 44   #adding new element w/o append

# print(person)

# print(person.items())
# print(person.keys())
# print(person.values())

# #MEMBERSHIP OPERATORS in, not in

# print(2 in mylist)

# #identity operators is, is not

# x = 5
# if type(x) is int:
#     print("x is an int")
# else:
#     print("x is not an int")

#FUNCTIONS
# def add(x,y):
#     print(x+y)

# add(9,12)

# def mysum(*numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     print(result)
# mysum(10, 20, 40, 50)

# def multiply(*numbers):
#     result = 1
#     for x in numbers:
#         result *= x
#     return result

# print(multiply(5,10))



# try:
#     x = int(input("First number"))
#     y = int(input("Second number"))
#     print(x/y)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Please enter a valid number!")
# finally:
#     print("DONE!")


# with open("file.txt", "r") as f:
#     content = f.read()

# print(content)

# file = open("file.txt", "r")
# content = file.read()
# file.close()

# print(content)

file = open("file.txt", "w")
file.write("Helloo !")
file.close()

file2 = open("file2.txt", "w")
file2.write("Very Good!")
file2.flush()

file = open("file.txt", "a")
file.write("Good afternoon")

file.close()

import os
os.mkdir("texty")
os.chdir("texty")
with open("myfile.txt", "w") as myfile:
    myfile.write("hello world") 
