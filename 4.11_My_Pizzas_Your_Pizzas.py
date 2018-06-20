# Beginning with Exercise 4.1, add to each list, create a new list and sentence, prove two lists. 
pizzas = ['cheese', 'pesto', 'hawaiian']
pizzas.append('cheesy pesto')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

friend_pizzas = ['cheese', 'pesto', 'hawaiian']
friend_pizzas.append('vegetarian')
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
