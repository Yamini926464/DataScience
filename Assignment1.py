# Basic String Manipulation:
# Assign the string "Hello, World!" to a variable and print it.
s1 = "Hello, World!"
print(s1)

# Create a string "Python Programming" and extract the first five characters using slicing.
s2 = "Python Programming"
print(s2[:5])

# String Methods:
# Given a string "python is fun", convert it to uppercase.
s3 = "python is fun"
print(s3.upper())

# Replace "fun" with "awesome" in the string "Python is fun".
s4 = "Python is fun"
print(s4.replace("fun", "awesome"))

# String Formatting:
# Use f-string formatting to create a message like "My name is John, and I am 25 years old.",
# where the name and age are variables.
name = "John"
age = 25
print(f"My name is {name}, and I am {age} years old.")

# Given a price of 49.99, format it to display only two decimal places.
price = 49.99
print(f"{price:.2f}")

# String Functions:
# Count the occurrences of the letter 'o' in "Hello, how are you?".
s5 = "Hello, how are you?"
print(s5.count('o'))

# Find the position of "world" in "Hello, world! Python is amazing.".
s6 = "Hello, world! Python is amazing."
print(s6.find("world"))

# Reverse and Check:
# Reverse the string "Python" using slicing.
s7 = "Python"
print(s7[::-1])

# Check if "madam" is a palindrome (a word that reads the same forward and backward).
s8 = "madam"
print(s8 == s8[::-1])