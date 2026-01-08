# Lesson 1 - setting up dev tools and intro to python
# print("Hello")

# Lesson 2 - Getting started with programming
# m=10
# print(m)

# username=input("Enter your name: ")
# print("Hello",username)

# Lesson 3 - Data types in python
# x=4
# y=5
# print(x+y)

# a="4"
# b="5"
# print(a+b)

# print(type(x))
# print(type(a))
 
# weight_in_kg=64.5
# print(type(weight_in_kg))

# is_married=False
# print(type(is_married))

# birth_year=input("Enter your birth year: ")
# age=2025-int(birth_year)
# print(age)

# Lesson 4 - Python operators 1

# Activity 1

# age_1=25
# age_2=35
# age_3=50
# sum=age_1+age_2+age_3
# average=sum/3
# print("average =",average)

 # Activity 2

# print("Welcome to ATM")
# amount=int(input("Enter amount (in multiples of 100) to withdraw :"))
# note_500=amount//500
# print("500 note count :",note_500)
# remaining_amount=amount%500
# note_200=remaining_amount//200
# print("200 note count :",note_200)
# remaining_amount=remaining_amount%200
# note_100=remaining_amount//100
# print("100 note count :",note_100)

# Activity 3

# print("Enter marks obtained (out of 100) in the below 4 subjects:")
# maths=int(input("Maths :"))
# english=int(input("English :"))
# computer=int(input("Computer :"))
# science=int(input("Science :"))
# total_marks_obtained=science+english+computer+science
# print(total_marks_obtained)
# total_percentage=total_marks_obtained/4
# print("Percentage =",total_percentage,"%")

# Lesson 5 - conditional statements
# Activity - 1

# first_number=int(input("Enter 1st number :"))
# second_number=int(input("Enter 2nd number :"))
# if first_number > second_number:
#     print("The first number is greater than the second number")
# elif second_number > first_number:
#     print("The second number is greater than the first number")
# else :
#     print("Both the numbers are equal")

 # Activity - 2

# cost_price=int(input("Enter cost price of the apple: "))
# selling_price=int(input("Enter selling price of the apple: "))
# profit=selling_price-cost_price

# if cost_price < selling_price:
#   print("You have made a profit of ₹",profit) 
# elif cost_price > selling_price:
#   print("You have made a loss of ₹",-profit)
# else :
#     print("you have not got any profit or loss")
    
#  Activity  3 -ask the user a number to check for even or odd

# number=int(input("Enter a number to check it is Even/Odd :"))
# if number % 2 == 0:
#     print("It is an Even Number")
# else :
#     print("It is an Odd Number")

#  Activity 4  
# a=10
# b=20
# condition=a>b
# print(condition)

# x=-10
# y=-20
# z=-30
# if x > 0 or y > 0 or z > 0:
#     print("Atleast 1 number is positive")
# else:
#     print("All numbers are negative or 0")

# Lesson 6 - Python operators 2

# Activity 1

# body_temperature=37
# if body_temperature != 37:
#     print("Not a healty body temperature")

# Activity 2 - BMI Calculator
# height=float(input("Enter your height in meters :"))
# weight=float(input("Enter your weight in kg :"))
# bmi=weight/(height*height)
# bmi=round(bmi,1)
# print("Your BMI is :",bmi)
# if bmi < 18.5:
#     print("You are underweight")
# elif bmi <= 24.9:
#     print("You are Healthy")
# elif bmi <= 29.9:
#     print("You are Overweight")
# else:
#     print("You are Obese")

# Activity 3 - ask a year from the user and check for leap year

# year=int(input("Enter a year to check if it a leap year :"))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("It is a Leap Year")
# else:
#     print("It is not a Leap Year")

# Lesson 7 - Python operators 3

# Activity 1 - demonstrate the left shift bitwise operator

a=10
a=a<<1
print(a)
# lesson paused
 
# Lesson 8 - Python challenges

# Activity 1 - three cyclists are riding at their respective speeds. Print the cyclists who are riding less than the average speed

# cyclist1_speed=int(input("Enter speed of cyclist 1 (km/h) :"))
# cyclist2_speed=int(input("Enter speed of cyclist 2 (km/h) :"))
# cyclist3_speed=int(input("Enter speed of cyclist 3 (km/h) :"))
# average=(cyclist1_speed+cyclist2_speed+cyclist3_speed)/3
# average=round(average,1)
# print("Average Speed :",average)
# if cyclist1_speed < average:
#     print("Cyclist 1 is slower than the average")
# if cyclist2_speed < average:
#     print("Cyclist 2 is slower than the average")
# if cyclist3_speed < average:
#     print("Cyclist 3 is slower than the average")

# Activity 2 - ask the user a dividend and a divisor. and then check if the dividend is divisible by the divisor or not. print appropriate message

# dividend=int(input("Enter a dividend :"))
# divisor=int(input("Enter a divisor :"))
# if dividend % divisor == 0:
#     print("It is divisible")
# else:
#     print("It is not divisible")
