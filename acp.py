# Lesson 1 - setting up dev tools and intro to python
# No acp for this lesson

# Lesson 2 - Getting started with programming
# No acp for this lesson

# Lesson 3 - Data types in python

# Question 1 - store 5 birthdays in the format dd/mm/yyyy in five separate variables. Name each variable after the corresponding person, and store the dates as strings

# hanveesh="26/06/2014"
# tinku="07/04/2014"
# arit="01/07/2014"
# johny="02/02/2014"
# evin="13/05/2014"
# print("Hanveesh -",hanveesh)
# print("Tinku -",tinku)
# print("Arit -",arit)
# print("Johny",johny)
# print("Evin -",evin)

# Question 2 - get two integers from the user and print their sum

# Num_1=input("Enter your 1st Number : ")
# No_1=int(Num_1)
# Num_2=input("Enter your 2nd Number : ")
# No_2=int(Num_2)
# total=No_1+No_2
# print("Total -",total)

# Question 3 - get two integers from the user. then divide the first integer by second integer. print the quotient and remainder. use appropriate variable names

# integer_1=int(input("Enter your first number :"))
# integer_2=int(input("Enter your second number :"))
# quotient=integer_1//integer_2
# remainder=integer_1%integer_2
# print("Quotient =",quotient)
# print("Remainder =",remainder)

# Question 4 - create a simple login system. Ask the user for a username and password, and check if they match stored values. If they match, print "Login successful", otherwise print "Username or password incorrect"

# correct_username="Evin"
# correct_password="1515"
# entered_username=input("Enter your username :")
# entered_password=input("Enter your password :")
# if entered_password == correct_password and entered_username == correct_username:
#     print("Login successful")
# else:
#     print("The Username or the password is incorrect")

# Question 5 - ask the user to enter a number that is a multiple of 9. Then print the appropriate response based on whether the number is a multiple of 9 or not

# entered_number=int(input("Enter a number to check if it is a multiple of 9 :"))
# if entered_number % 9 == 0:
#     print("it is divisible by 9")
# else:
#     print("it is not divisible by 9")

# Question 6 - store three numbers in three variables (a, b, c) respectively. then swap a, b and c. meaning a should have the value of b, b should have the value of c and c should have the value of a. finally print the values of a, b and c. hint: you can use a temporary variable to help with the swapping

a=10
b=20
c=30
print(a,b,c)
temp_value=a
a=b
b=c
c=temp_value
print(a,b,c)