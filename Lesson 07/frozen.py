print("\t\t\t\n FROZENSET")
print("\nA frozenset is an immutable version of a set.\n")

# Creating a frozenset (Duplicate values are ignored)
fs = frozenset([1, 5, 5])  
empty_fs = frozenset()  # Creating an empty frozenset

print("Frozen Set:", fs)  # Output: frozenset({1, 5})
print("Type of fs:", type(fs))  # Output: <class 'frozenset'>


print("\t\t\t\nPROPERTIES OF FROZENSET:\n")
print("""
      1. Frozensets are unordered => Elements do not maintain any specific order
      2. Frozensets are unindexed => Cannot access elements by index like fs[0]
      3. Frozensets are immutable => Cannot add or remove elements after creation
      4. Frozensets cannot contain duplicate values
      """)

# OPERATIONS ON FROZENSET

# • len(fs): Returns the number of unique elements in the frozenset
print("The Length of frozen set is:", len(fs))  # Output: 2

# Creating new frozensets for set operations
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4, 5])

# • fs1.union(fs2): Returns a new frozenset containing all unique elements
print("This is Union of 2 frozen sets:", fs1.union(fs2))  # Output: frozenset({1, 2, 3, 4, 5})

# • fs1.intersection(fs2): Returns a new frozenset containing only common elements
print("This is intersection of 2 frozen sets:", fs1.intersection(fs2))  # Output: frozenset({2, 3})

# ❌ ERROR: The following operations are **not allowed** on a frozenset
# fs.add(6)     # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)  # AttributeError: 'frozenset' object has no attribute 'remove'
# fs.pop()      # AttributeError: 'frozenset' object has no attribute 'pop'
