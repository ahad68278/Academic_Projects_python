##############################################################
#Task 1: User Input and Conditional Logic 

age=int(input("Enter age : "))
language=input("Enter favorite programming language : ")
if age < 18:
    print("You are a young programmer learning " + language)
elif age >= 18:
    print("Welcome to the world of AI with " + language)
if language == 'python':
    print("You're on the right track to AI!")

##############################################################
#Task 2: Control Structures and Loops 

#Using WHILE_LOOP
print(" ")
print("Using WHILE_LOOP")
num=int(input("Enter the number for table : "))
c=1
while c<=10:
    b=num*c
    print(num , " * " , c , " = ",b)
    c += 1
print(" ")
if num % 2 == 0:
    print(num , " is Even")
else:
    print(num , " is Odd")

#Using FOR_LOOP
print(" ")
print("Using FOR_LOOP")
num = int(input("Enter the number : "))
for i in range(1,11):
    b = num * i
    print(  num , " * ", i , " = " , b)
print(" ")
if num % 2 == 0:
    print(num , " is Even")
else:
    print(num , " is Odd")
print(" ")
##############################################################

#Task 3: Functions and Lists

def count_odd_numbers(number):
    cnt = 0
    for num in number:
        if num % 2 != 0:
            cnt += 1
    return cnt
    
numbers = []
for i in range (5):
    num = int(input ("Enter Numbers to check Even/Odd: "))
    numbers.append(num)
print("Numbers : " ,numbers)
odd=count_odd_numbers(numbers)
print(f"Odd Count Numbers : {odd}")

##############################################################