print("\t\t\t\n LISTS IN PYTHON")
print("\nLists are containers used to store multiple values of different data types, similar to arrays.\n")

# Creating a list with different data types
friends = ["Apple", "Orange", "Mango", 3, 6, False, "FARRY"]
print("\nOriginal List:", friends)

# Accessing list elements by index
print("\nElement at index 2:", friends[2])

# Modifying an element in the list
friends[2] = "Berry"
print("\nModified List:", friends)

print("\t\t\t\nLIST INDEXING & SLICING")
l1 = [7, 9, "Harry"]
print("\nElement at index 0:", l1[0])  # Output: 7
print("\nElement at index 1:", l1[1])  # Output: 9
print("\nList slice from index 0 to 2:", l1[0:2])  # Output: [7, 9]

print("\t\t\t\nLIST METHODS")

# Append - Adds an item at the end
friends.append("Harry")
print("\nAfter append:", friends)

# Sort - Arranges list in ascending order
li = [1, 94, 56, 78]
li.sort()
print("\nSorted list:", li)

# Insert - Adds an item at a specific index
friends.insert(5, 78907)  # 5 is index, 78907 is the new element
print("\nAfter insert:", friends)

# Pop - Removes and returns the element at the specified index
fri = ["Apple", "Orange", "Mango", 3, 6, False, "FARRY"]
popped_element = fri.pop(4)
print("\nPopped element:", popped_element)
print("\nAfter pop:", fri)

# Remove - Removes the first occurrence of a value
values = [1, 3, "FARRY"]
values.remove(3)
print("\nAfter remove:", values)

# Extend - Adds elements from another list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("\nExtended List:", list1)

# Reverse - Reverses the order of elements
list1.reverse()
print("\nReversed List:", list1)

# Count - Counts occurrences of a specific element
nums = [1, 2, 2, 3, 4, 2, 5]
print("\nCount of 2 in list:", nums.count(2))

# Index - Returns the index of the first occurrence of an element
print("\nIndex of element 3:", nums.index(3))

# Copy - Creates a shallow copy of the list
copy_list = friends.copy()
print("\nCopied List:", copy_list)
