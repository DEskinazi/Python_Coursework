# Store a list of places to visit
vacations = ['Argentina', 'Turkey', 'Cuba', 'Poland', 'Netherlands']

# Print this list in its original order
print("Here is the original list:")
print(vacations)

# Print a temporary list in alphabetical order

print("\nHere is a sorted list:")
print(sorted(vacations, reverse=True))

# Print original list

print("\nHere is the original list:")
print(vacations)

# Print a list in reverse

print("\nHere is the list in reverse order:")
vacations.reverse()
print(vacations)

# Reverse the order of the list
print("\nHere is the list in its original order:")
vacations.reverse()
print(vacations)

# Alphabetize the original list
print("\nHere is another sorted list:")
vacations.sort()
print(vacations)

# Reverse the alphabetized list. sorted using reverse=True argument.
print("\nHere is the list in reverse alphabetical order:")
vacations.sort(reverse=True)
print(vacations)



