
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

mylist =[1,2, "dog", 60, True, 9.87]
print(mylist[:3])

mylist[3] = "cat"
print(mylist)

for x in mylist:
    print(x)

mylist2 = [1,2,3,4,5]
for y in mylist2:
    print(2**y)