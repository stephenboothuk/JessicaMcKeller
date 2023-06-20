# Create and populate a list
your_list = ["a", "b", "c", "elephant"]
# Display the length of the list
print(len(your_list))
# Display the type of the list: <class 'List'>
print(type(your_list))
# Is the string 'a' in the list
print('a' in your_list)
# Is the string elephant in the list
print('elephant' in your_list)
# Is the string e in the list, not this is false as it is looking for a whole string that is e
print('e' in your_list)
# Is the string z in the list
print('z' in your_list)
# Is the string z not in the list
print('z' not in your_list)
# Display the first (position zero) item in the list
print(your_list[0])
# Is the string e in the fourth element (position 3) of the list
print('e' in your_list[3])

# Add a new item to the end of th elist
your_list.append("d")
# Display the new length of the list
print(len(your_list))
# Create an empty list
her_list = []
# Display that the list has zero entries
print(len(her_list))

# Create and populate a new list
names = ["Alice", "Amy"]
print(names)
names.append("Adam")
print(names)
# Replace Alice
names[0] = "Jimmy"
print(names)
# Replace Adam
names[2] = "Rachel"
print(names)
# Add some more names
names.append("Tim")
names.append("Bob")
names.append("Alexis")
print(names)
# How many items
print(len(names))
# Get last item
# hard way
print(names[len(names) - 1])
# Easy way
print(names[-1])
