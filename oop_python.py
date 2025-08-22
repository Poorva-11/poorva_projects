# def hello():
#     print("Hello")
#
# x=1
# print(hello())
# print(type(hello))
# print(type(x))

# string = "hello"
# print(string.upper())

# #creating a class
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(name,age)
#
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def add_one(self,x):
#         return x+1
#
#     def bark(self):
#         print("bark")
#
#     def set_age(self,age):
#         self.age = age
#
# d = Dog("Poorva",21)
# d.set_age(25)
# print(d.get_name())
# print(d.get_age())
# d1 = Dog("Bob",12)
# print(type(d))
# print(d.add_one(4))
# d.bark()

# #multiple classes
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         print(name,age,grade)
#
#     def get_grade(self):
#         return self.grade
#
# class course:
#     def __init__(self, course_name, max_students):
#         self.course_name = course_name
#         self.max_students = max_students
#         self.students = []
#
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#
#     def avg_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#             return value / len(self.students)
#
#
# s1 = Student("John", 24, 91)
# s2 = Student("Tom", 21, 51)
# s3 = Student("bob", 24, 100)
#
# course = course("Python", 3)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# print(course.avg_grade())
# print(course.students[0].name, course.students[0].age, course.students[0].grade)
# print(course.students[1].name, course.students[1].age, course.students[1].grade)
# print(course.students[2].name, course.students[2].age, course.students[2].grade)

# #Inheritance
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)
#
#     def speak(self):
#         print("Pets speak")
#
# class Dog(Pet):
#     def speak(self):
#         print("bark")
#
# class Cat(Pet):
#     def speak(self):
#         print("meow")
#
# class Fish(Pet):
#     pass
#
# p = Pet("pet", 20)
# p.show()
# p.speak()
# c = Cat("John", 20)
# c.show()
# c.speak()
# d = Dog("bob", 20)
# d.show()
# d.speak()
# f = Fish("poo",89)
# f.show()
# f.speak()

# #Super class
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)
#
#     def speak(self):
#         print("Pets speak")
#
# class Dog(Pet):
#     def speak(self):
#         print("bark")
#
# class Cat(Pet):
#     def __init__(self, name, age,color):
#         super().__init__(name, age)
#         self.color = color
#
#     def speak(self):
#         print("meow")
#
#     def show(self):
#         print(self.name, self.age, self.color)
#
# class Fish(Pet):
#     pass
#
# p = Pet("pet", 20)
# p.show()
# p.speak()
# c = Cat("John", 20,"black")
#
# c.show()
# c.speak()
# d = Dog("bob", 20)
# d.show()
# d.speak()
# f = Fish("poo",89)
# f.show()
# f.speak()

# #Class Attributes
# class Person:
#     numer_of_people = 0
#     def __init__(self, name):
#         self.name = name
#         Person.numer_of_people += 1
#
#     # Class method
#     @classmethod
#     def number_of_people(cls):
#         return cls.numer_of_people
#
#     @classmethod
#     def add_person(cls):
#         cls.numer_of_people += 1
#
# p1 = Person("John")
# p2 = Person("bob")
#
# print(Person.numer_of_people)
#
#
# Person.numer_of_people = 8
# print(p1.numer_of_people)
# print(p2.numer_of_people)

# #Static Method
# class Math:
#
#     @staticmethod
#     def add5(x):
#         return x + 5
#
#     @staticmethod
#     def add10(x):
#         return x + 10
#
#     @staticmethod
#     def pr():
#         print("run")
#
# print(Math.add5(5))
# print(Math.add10(10))
# Math.pr()

# #Polymorphism
# class Dog:
#     def speak(self):
#         return "Woof!"
#
# class Cat:
#     def speak(self):
#         return "Meow!"
#
# d = Dog()
# c = Cat()
# print(d.speak())
# print(c.speak())

# #Abstraction
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#
# class Car(Vehicle):
#     def start_engine(self):
#         print("Car Engine Started")
#
# c = Car()
# c.start_engine()

# #Encapsulation:Restricting direct access to variables, providing methods to access them.
# class BankAccount:
#     def __init__(self):
#         self.__balance = 100#private variable
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def get_balance(self):
#         return self.__balance
#
# acc = BankAccount()
# acc.deposit(1000)
# print(acc.get_balance())

