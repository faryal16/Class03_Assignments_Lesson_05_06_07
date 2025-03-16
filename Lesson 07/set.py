print("\t\t\t\n SETS")
print("\nSet is a collection of non-repetitive elements.\n")

s = {1, 5, 5}  # Duplicate values are ignored
e = set()  # This is an empty set (NOT {} because {} creates an empty dictionary)
s.add(566)  # Adding an element to the set

print(s)  # Output: {1, 5, 566} (Order is arbitrary)
print(type(s))  # Output: <class 'set'>


print("\t\t\t\nPROPERTIES OF SETS:\n")
print("""
      1. Sets are unordered => Elements do not maintain any specific order
     2. Sets are unindexed => Cannot access elements by index like s[0]
     3. Sets are immutable => Once created, elements cannot be modified (only added/removed)
     4. Sets cannot contain duplicate values
      """) 
# 

# OPERATIONS ON SETS

# • len(s): Returns the number of unique elements in the set
print("The Length of sets is :",len(s))  # Output: 3

# • s.remove(x): Removes the element x from the set; raises an error if x is not found
s.remove(5)  
print("The Value 5 has been removed from the set.")  

# • s.pop(): Removes and returns an arbitrary element from the set
removed_element = s.pop()
print("Removed:", removed_element)

# • s.clear(): Empties the set
s.clear()
print(" Now The set is clear or empty :",s)  # Output: set()

# Creating a new set for union & intersection operations
s1 = {1, 2, 3}
s2 = {2, 3, 4, 5}

# • s1.union(s2): Returns a new set containing all unique elements from both sets
print("This is Union of 2 sets",s1.union(s2))  # Output: {1, 2, 3, 4, 5}

# • s1.intersection(s2): Returns a new set containing only common elements
print("This is intersection of 2 sets",s1.intersection(s2))  # Output: {2, 3}
