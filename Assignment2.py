# 1. Even or Odd Checker
# Write a Python program that takes an integer input from the user and determines whether the number is even or odd using an if-else statement.

num = int(input("Enter an integer to check even or odd: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("-" * 40)

# 2. Find the Largest Number
# Create a Python program that takes three numbers as input and uses if-else conditions to find and display the largest number.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

print("-" * 40)

# 3. Number Classification
# Write a program that takes a number input and checks if the number is positive, negative, or zero using if-elif-else conditions.

num = float(input("Enter a number to classify: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("-" * 40)

# 4. Sum of Numbers in a Range
# Write a Python program that takes two numbers (start and end) as input and uses a for loop to compute and display the sum of all numbers in that range.

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
total = 0

for i in range(start, end + 1):
    total += i

print("Sum of numbers in range:", total)

print("-" * 40)

# 5. Printing a Multiplication Table
# Develop a Python program that takes an integer as input and prints its multiplication table from 1 to 10 using a for loop.

num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("-" * 40)

# 6. Counting Vowels in a String
# Write a Python script that takes a string input from the user and uses a for loop to count the number of vowels (a, e, i, o, u) present in the string.

text = input("Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels in the string:", count)

print("-" * 40)

# 7. Factorial Calculator
# Create a Python program that takes a positive integer as input and calculates its factorial using a for loop.

num = int(input("Enter a positive integer to find its factorial: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")

print("-" * 40)

# 8. FizzBuzz Game
# Write a Python program that prints numbers from 1 to 50.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
