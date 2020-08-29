# print a pattern

print "--" * 50
print("Assignment 2.z : To print a pattern ")
print "--" * 50

for i in range(1,6,1):
    print ("*")*i

for i in range(4,0,-1):
    print ("*")*i

# 2 to reverse a word after accepting input from user
print("\n")
print "--" * 50
print("Assignment 2.b : To reverse a word after accepting input from user ")
print "--" * 50

Wordrev = str(input("Enter a Word :"))
print(Wordrev[::-1])