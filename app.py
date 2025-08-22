#Printing Statements
# print("Hello World")
# print("      /|")
# print("     / |")
# print("    /  |")
# print("   /___|")

# print("Poorva\nPatil")
# print("\"")
# print("\hello")

#Strings
# name = "poorva "
# print(name)
# print(name.upper())
# print(name.upper().isupper())
# print(name+"Patil")
# print(len(name))
# print(name[1:3])
# print(name.index("r"))
# name1 = "sinchan nohara"
# print(name1)
# print(name1.replace("nohara","Patil"))

# #Math Operators
# from math import *
# n = 2
# print(type(n))
# print(2+3/4%9*4)
# print(str(2))
# print(abs(-9.7))
# print(2**3)
# print(pow(2,3))
# print(max(9,8,4,3))
# print(ceil(9.5))
# print(sqrt(9))

# #Taking input from user
# name = input("Enter your name:")
# n = int(input("Enter your age:"))
# print("Name is:",name,"Age is:",n)
#
# n1 = int(input("Enter number1:"))
# n2 = int(input("Enter number2:"))
# print(n1+n2)

#Lists
# num = [1,2,3,4,5,"poo",9.8]
# print(num)
# print(num[2])
# print(num[-2])
# print(num[1:3])
# num[1] = 6
# print(num)

# lucky_num = [1,2,3,4,5,-9,68,8]
# friends = ["Poo","Tom","Oggy"]
# print(friends)
# friends.append("Jim")
# print(friends)
# friends.insert(1,"poorva")
# print(friends)
# friends.remove("Jim")
# print(friends)
# friends.pop()
# print(friends)
# print(friends.index("Poo"))
# print(friends.count("Poo"))
# lucky_num.sort()
# print(lucky_num)
# friends2 = friends.copy()
# print(friends2)

from calendar import month
from zipfile._path import Translator


#Tuples:immutable
# coordinates = (4,5)
# print(coordinates[0])

#Functions
# def say_hi(name,age):
#     print("HI", name,age)
#
# say_hi("Poorva",90)
# say_hi("Poo",80)
#
# def cube(num):
#     print(num*num)
#     return num*num*num
#     print("Poo")
# print(cube(5))
#
#If Statements
# is_male = False
# if is_male:
#     print("You are Male")
#
# is_male = False
# if is_male:
#     print("You are Male")
# else:
#     print("You are not Male")
#
#or and
# is_male = True
# is_tall = False
# if is_male or is_tall:
#     print("You are Male and Tall")
# else:
#     print("You are not Male and Tall")
#
# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("You are Male and Tall")
# else:
#     print("You are not Male and Tall")

# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("You are Male and Tall")
# elif is_tall and not(is_male):
#     print("You are not Male and Tall")
# elif is_male and not(is_tall):
#     print("You are Male and not Tall")
# else:
#     print("You are not Male and not Tall")
#
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(5,6,7))
#
#Calculator
# num1 = int(input("Enter a number1: "))
# op = input("Enter operator: ")
# num2 = int(input("Enter a number2: "))
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "**":
#     print(num1 ** num2)
# elif op == "//":
#     print(num1 // num2)
# elif op == "%":
#     print(num1 % num2)
# else:
#     print("Invalid operator")
#
# #Dictionaries
# monthConversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "June",
#     "Jul" : "July",
#     "Aug" : "August",
#     "Sep" : "September",
#     "Oct" : "October",
#     "Nov" : "November",
#     "Dec" : "December"
# }
#
# print(monthConversions["Jan"])
# print(monthConversions.get("poo"))
# print(monthConversions[input("Enter month: ")])

#WhileLoop
# i = 1
# while i <= 10:
#     print(i)
#     i+=1
# print("Done with loop")
#
#Gusseing Game
# secret_word = "Poorva"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guess = False
#
# while guess != secret_word and not(out_of_guess):
#     if guess_count < guess_limit:
#         guess = input("Guess a correct word: ")
#         guess_count += 1
#     else:
#         out_of_guess = True
# if out_of_guess:
#     print("Sorry, you loose")
# else:
#     print("You guessed", guess)

#Forloop
# for letter in "Poorva Patil":
#     print(letter)
#
# friends = ["Poo","Tom","Oggy"]
# for friend in friends:
#     print(friend)
# for index in range(len(friends)):
#     print(friends[index])
#     print(index)
#
#Exponent function
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for i in range(pow_num):
#         result = result * base_num
#     return result
# print(raise_to_power(2, 3))


#2D list and nested loops
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10]
# ]
# print(number_grid)
# print(type(number_grid))
# print(number_grid[0])
# print(number_grid[1][2])
#
# for row in number_grid:
#     print(row)
#
# for row in number_grid:
#     for col in row:
#         print(col)

# #Build Translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "aeiouAEIOU":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase: ")))

#Try Except
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Please enter a number")
#
# try:
#     number1 = int(input("Enter a number: "))
#     number2 = int(input("Enter a number: "))
#     print(number1/number2)
# except ZeroDivisionError:
#     print("You can't divide by zero")

# #Files:Reading to Files
# employee_file=open("employee.txt","r")
# print(employee_file.readable())
# print(employee_file.read())
# # print(employee_file.readlines())
# print(type(employee_file))
# print(type(employee_file.read()))
#
# # for line in employee_file.readlines():
# #     print(line)
#
# employee_file.close()

#Writting to Files
# employee_file1 = open('employee.txt1', 'w')
# employee_file1.write("My name is : Poorva")
# employee_file1.write("\nMy surname is : Patil")
# employee_file1.close()
#
# employee_file = open('employee.txt', 'a')
# employee_file.write("\nToby = HR")
#
# employee_file.close()

#Modules and PIP
# import app1
# from app1 import say_hello

# #Classes and objects
# from student import student
# student1 = student("Poorva",21,8.8)
# student2 = student("James",21,3.1)
# print(student1.name)
# print(student1.age)
# print(student1.gpa)
# print(student2.name,student2.age,student2.gpa)
# #object function
# print(student2.on_honor_roll())

# #Inheritance
# from chef import Chef
# from chinesechef import chinesechef
#
# mychef = Chef()
# mychef.make_special_dish()
#
# print()
#
# mychinesechef = chinesechef()
# mychinesechef.make_special_dish()
# mychinesechef.make_fried_rice()
# mychinesechef.make_rice()

# #Quiz
# # Define the Question class
# class Question:
#     def __init__(self, prompt, answer):
#         self.prompt = prompt
#         self.answer = answer
#
# # List of question prompts
# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Pink\n(c) Yellow\n\n",
#     "What color are bananas?\n(a) Red/Green\n(b) Pink\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Red\n(b) Pink\n(c) Yellow\n\n",
# ]
#
# # List of Question objects with correct answers
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "a"),
# ]
#
# # Function to run the quiz
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer.lower() == question.answer.lower():
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
#
# # Run the quiz
# run_test(questions)

i = 1
while i <= 10:
    if i == 3:
        i = i + 1
        break
    print(i)
    i = i + 1
print()

i = 1
while i <= 10:
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1

