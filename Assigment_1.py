# 1) Program to identify a number divisible 7 and not a multiple of 5
print "--" * 50
print("Assignment 1.a : Program to identify a number divisible 7 and not a multiple of 5 ")
print "--" * 50
print("\n")
m = []
for i in (range(2000, 3201, 1)):
    if (i % 7 == 0) and (i % 5 != 0):
        m.append(i)
print (m)

# 2) Accept user Firstname and Lastname and print in reverse order
print("\n")
print "--" * 50
print("Assignment 1.b : Accept user Firstname and Lastname and print in reverse order")
print "--" * 50
print("\n")
UserName = []
FirstName = str(input("Please enter your First name with single quotes : "))
LastName = str(input("Please enter your Last name with single quotes : \n"))

UserName.append(FirstName)
UserName.append(LastName)

RevUserName = []
for i in UserName[::-1]:
    RevUserName.append(i)

print(FirstName[::-1] + " " + LastName[::-1])
print(UserName[1] + " " + UserName[0])

# 3) Program to find vol of sphere with diameter 12
print("\n")
print "--" * 50
print("Assignment 1.c : Program to find vol of sphere with diameter 12 ")
print "--" * 50
print("\n")
SpDiameter = 12
pi = 22/7

Vol_of_Sp = (4/3) * pi * ((SpDiameter/2) ** 3)

print "Volume of square with diameter 12 : ", Vol_of_Sp

