#Basic Operations:
# Create a set with at least five different numbers
numbers = {1, 3, 5, 7, 9}
print("Original Set:", numbers)

# Add an element
numbers.add(11)
print("After Adding 11:", numbers)

# Remove an element
numbers.remove(3)
print("After Removing 3:", numbers)

# Check if an element exists
print("Is 5 in the set?", 5 in numbers)

#set Operations:
# Define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print("Union:", A | B)

# Intersection
print("Intersection:", A & B)

# Difference
print("Difference (A - B):", A - B)

# Subset check
print("Is A a subset of B?", A.issubset(B))

#Unique elements:
# List with duplicates
nums = [1, 2, 2, 3, 4, 4, 5]

# Convert to set to remove duplicates
unique_nums = set(nums)
print("Unique Elements:", unique_nums)

#Mathematical Applications:
# Students in Course A and Course B
course_A = {"Alice", "Bob", "Charlie"}
course_B = {"Charlie", "David", "Eve"}

# Students in both courses
both_courses = course_A & course_B
print("Students in both courses:", both_courses)

# Common elements in three sets
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
set3 = {0, 2, 3, 6}

common = set1 & set2 & set3
print("Common elements in all three sets:", common)

#Set Comprehension:
# Squares of numbers from 1 to 10
squares = {x ** 2 for x in range(1, 11)}
print("Squares from 1 to 10:", squares)

#Frozen Sets:
# Frozensets are immutable sets
frozen = frozenset([1, 2, 3, 4])
print("Frozenset:", frozen)

# You cannot add or remove elements from a frozenset
# frozen.add(5) → would raise an AttributeError

# But you can use it in a dictionary key or set
frozen_set_dict = {frozen: "immutable set"}
print("Using frozenset as a dictionary key:", frozen_set_dict)
