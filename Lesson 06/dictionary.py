print("\t\t\t\n DICTIONARIES")
print("\nDictionaries store key-value pairs, allowing fast lookup of values based on unique keys.\n")


print("\t\t\t\nPROPERTIES OF DICTIONARIES:\n")
print("""
    1. Dictionaries store data in key-value pairs.
    2. Keys must be unique and immutable (strings, numbers, tuples).
    3. Values can be of any data type.
    4. Dictionaries are unordered in Python versions < 3.7, but ordered from 3.7+.
    5. Dictionaries are mutable (modifiable).
""")
# Creating a dictionary
student = {
    "name": "Harry",
    "age": 21,
    "grade": "A",
    "subjects": ["Math", "Science"],
    "is_passed": True
}

print(student)
# Accessing values using keys
print("\nStudent Name:", student["name"])  # Output: Harry
print("\nStudent Age:", student["age"])  # Output: 21

# Modifying dictionary values
student["grade"] = "A+"  # Updating a value
print("\nUpdated Grade:", student["grade"])  # Output: A+



# Dictionary METHODS
print("\n\t\tDictionary METHODS")
# keys(): Returns all dictionary keys
print("\nKeys:", student.keys())  # Output: dict_keys(['name', 'age', 'grade', 'subjects', 'is_passed'])

# values(): Returns all dictionary values
print("\nValues:", student.values())  # Output: dict_values(['Harry', 21, 'A+', ['Math', 'Science'], True])

# items(): Returns all key-value pairs as tuples
print("\nItems:", student.items())  
# Output: dict_items([('name', 'Harry'), ('age', 21), ('grade', 'A+'), ('subjects', ['Math', 'Science']), ('is_passed', True)])

# get(): Retrieves a value without causing an error if the key is missing
print("\nStudent Grade:", student.get("grade"))  # Output: A+
print("\nGPA (missing key):", student.get("GPA", "Not Available"))  # Output: Not Available

# pop(): Removes a key-value pair and returns the value
removed_value = student.pop("is_passed")
print("\nRemoved Value:", removed_value)  # Output: True

# update(): Merges another dictionary into the existing one
extra_info = {"school": "XYZ Academy", "age": 22}  # Updating existing key 'age'
student.update(extra_info)
print("\nUpdated Dictionary:", student)

# popitem(): Removes and returns the last inserted key-value pair
last_item = student.popitem()
print("\nPopped Item:", last_item)

# clear(): Removes all dictionary elements
student.clear()
print("\nCleared Dictionary:", student)  # Output: {}

# Nested Dictionary
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 21}
}
print("\nNested Dictionary:", students)

# Dictionary comprehension (Creating a dictionary dynamically)
squares = {x: x**2 for x in range(1, 6)}
print("\nSquares Dictionary:", squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
