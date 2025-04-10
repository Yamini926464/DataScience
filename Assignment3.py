# Tuple Creation
my_tuple = (42, "hello", 3.14, "world", 100)
print("Original tuple:", my_tuple)

# Accessing Elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Second last element (negative indexing):", my_tuple[-2])

# Tuple Slicing
print("First three elements:", my_tuple[:3])
print("Last two elements:", my_tuple[-2:])

# Tuple Operations
another_tuple = (200, "new")
concatenated = my_tuple + another_tuple
print("Concatenated tuple:", concatenated)

repeated = my_tuple * 2
print("Repeated tuple:", repeated)

# Tuple Methods
print("Index of 'hello':", my_tuple.index("hello"))
print("Count of 42:", my_tuple.count(42))

# Tuple Immutability
try:
    my_tuple[0] = 999  # This will raise an error
except TypeError as e:
    print("Error when trying to change tuple element:", e)

print("Explanation: Tuples are immutable, meaning their elements cannot be changed once created.")

# Tuple Packing and Unpacking
packed_tuple = ("Alice", 25, "Engineer")
name, age, profession = packed_tuple
print("Unpacked values:")
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# Tuple Iteration
print("Iterating through my_tuple:")
for element in my_tuple:
    print(element)

# Tuple Usage - Function returning multiple values using a tuple
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count else 0
    return total, count, average

stats = calculate_stats([10, 20, 30, 40, 50])
print("Returned stats tuple:", stats)
