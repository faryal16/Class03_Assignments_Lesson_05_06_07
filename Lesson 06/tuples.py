print("\t\t\t\n TUPLES")
print("\nTuples are immutable containers used to store a collection of values of any data type.\n")

# Creating a tuple
fruits = ("Apple", "Orange", "Mango", 3, 6, False, "FARRY")
print(fruits[2])  # Output: Mango

# Trying to change a tuple element (will cause an error because tuples are immutable)
# fruits[2] = "Berry"  ❌ This will raise an error

print("\t\t\t\nPROPERTIES OF TUPLES:\n")
print("""
    1. Tuples are ordered => Elements have a fixed position.
    2. Tuples are indexed => You can access elements using indexes like t[0].
    3. Tuples are immutable => Cannot modify elements after creation.
    4. Tuples allow duplicate values.
""")

# TUPLE INDEXING & SLICING
t1 = (7, 9, "Harry")
print("\nIndexing of Tuple: " , t1)
print(t1[0])  # Output: 7
print(t1[1])  # Output: 9
# print(t1[70])  ❌ This will cause an IndexError
print(t1[0:2])  # Output: (7, 9) - Tuple slicing

# TUPLE METHODS

# count(): Returns the number of times a value appears in the tuple
numbers = (1, 2, 3, 2, 2, 4, 5)
print("\nCount of 2:", numbers.count(2))  # Output: 3

# index(): Returns the first index of a specified value
print("\nIndex of 3:", numbers.index(3))  # Output: 2

# len(): Returns the total number of elements in the tuple
print("\nLength of tuple:", len(numbers))  # Output: 7

# Concatenation: Joining two tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50)
merged_tuple = tuple1 + tuple2
print("\nMerged Tuple:", merged_tuple)  # Output: (10, 20, 30, 40, 50)

# Nested Tuples
nested_tuple = (("A", "B", "C"), (1, 2, 3))
print("\nNested Tuple:", nested_tuple)  # Output: (('A', 'B', 'C'), (1, 2, 3))

# Checking if an element exists in a tuple
print("\nIs 'Mango' in fruits?", "Mango" in fruits)  # Output: True

# Converting a list to a tuple
list_data = [10, 20, 30, 40]
converted_tuple = tuple(list_data)
print("\nConverted Tuple:", converted_tuple)  # Output: (10, 20, 30, 40)

# Tuple Unpacking
a, b, c = (10, 20, 30)
print("\nUnpacked Values:", a, b, c)  # Output: 10 20 30
