#Classes:
#Define a class Person with attributes name and age. Create an object of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Create a class Rectangle with attributes length and width. Include a method to calculate the area of the rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#Implement a BankAccount class with methods to deposit and withdraw money. Ensure that the balance does not go negative.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")
#Design a class Student with attributes name and marks. Include a method that calculates the grade based on marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"
#Write a Vehicle class with a method description() that prints the vehicle type. Create a subclass Car that inherits from Vehicle and overrides the description() method.
class Vehicle:
    def description(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def description(self):
        print("This is a car.")

#Functions:
#Write a function add_numbers(a, b) that returns the sum of two numbers.
def add_numbers(a, b):
    return a + b

#Create a function factorial(n) that calculates the factorial of a given number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#Implement a function is_prime(n) that checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#Define a function reverse_string(s) that returns the reverse of a given string.
def reverse_string(s):
    return s[::-1]

#Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence



