# Using a previous program, add lines to the end that show how slices operate
furry_animals = ['cheetah', 'leopard', 'bear', 'dog']
for furry_animal in furry_animals:
	print(furry_animal)
	print("A " + furry_animal.lower() + " is a furry animal.\n")

print("These animals all have fur.")

print("The first three animals in the list are " + str(furry_animals[0:3]) + ".")