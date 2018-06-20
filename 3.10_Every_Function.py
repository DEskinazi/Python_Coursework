# Create any list and work with elements in a list.

# Store items in a list
legumes = ['pinto', 'lima', 'kidney', 'navy']
print(legumes)

# Access an items according to index position
print(legumes[3])
print(legumes[1])

# Use any of the values in a lesson
message = "\nWe usually use " + legumes[0] + " beans in our tacos."
print(message)

# Changing an item in the list
legumes[3] = 'black'
print(legumes)

# Adding an element to a list
legumes.append('garbanzo')
print(legumes)

# Insert an element in the list
legumes.insert(0, 'lentils')
print(legumes)

# Removing an item using del statement
del legumes[0]
print(legumes)

# Remove an item using pop() Method
popped_legumes = legumes.pop(0)
print(legumes)

# Pop an items from any position
favorite_beans = legumes.pop(2)
print("The beans I love to eat with Cuban food are " + favorite_beans + " beans.")

# Removing an item by value
legumes.remove('garbanzo')
print(legumes)

# Storing a value in a new variable and working with that later
red_beans = 'kidney'
legumes.remove(red_beans)
print(legumes)
print("\n" + red_beans.title() + " beans are red.")

# Adding items back into a list
legumes.append('kidney')
legumes.append('black')
legumes.append('garbanzo')
legumes.append('pinto')
legumes.append('lentils')
print(legumes)

# Organizing a list
legumes.sort()
print(legumes)

# Reverse list order permanently
legumes.sort(reverse=True)
print(legumes)

# Sorting a list temporarily
print("Here is the original list:")
print(legumes)

print("\nHere is a sorted list")
print(sorted(legumes))

print("\nHere is the original list again in reverse")
print(sorted(legumes, reverse=True))

# Find the length of the list
print(len(legumes))
