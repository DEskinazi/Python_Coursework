# Store buffet items in a tuple. Use a for loop to print the items.

buffet_items = ('corn bread', 'pizza', 'salad', 'soup')
print("This buffet offers many items including:")
for buffet_item in buffet_items:
	print(buffet_item.title())

# Try to edit the list to prove that Python rejects change to a tuple. Success!
buffet_items.append('dessert')