# create an empty list
mylist = []

# Append elements
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)

# Insert 15 at the second position
mylist.insert(1,15)

# Extend the list with another list
mylist.extend([50,60,70])

# Remove the last element
mylist.pop()

# Sort the list in ascending order
mylist.sort()

# Find and print the index of 30
indexof30 = mylist.index(30)
print("The index of 30 is:", indexof30)