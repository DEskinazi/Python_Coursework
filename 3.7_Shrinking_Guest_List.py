# Using the program in Exercise 3.6, let people know that the new table won't arrive on time and I have to reduce the number of attendees using pop().
guests = ['chuchi', 'morris', 'celia']
print("Please join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")

print("I found a bigger dinner table and we can now invite more guests.")

guests.insert(0, 'abraham')

guests.insert(2, 'tio vitali')

guests.append('luba')

# Print a new invitation for each guest.
print("Please join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")
print("Please join me for my party, " + guests[3].title() + ".")
print("Please join me for my party, " + guests[4].title() + ".")
print("Please join me for my party, " + guests[5].title() + ".")


# Let people know that your table won't arrive and you can't have as many guests as you thought. 

print("I just found out my new table will not arrive on time. I can only invite two people.")
uninvited = guests.pop()
uninvited = guests.pop()
uninvited = guests.pop()
uninvited = guests.pop()

print("I hope you can still join me for my party, " + guests[0].title() + ". I only have room for you and one other guest.")
print("I hope you can still join me for my party, " + guests[1].title() + ". I only have room for you and one other guest.")


# Delete the rest of the guests

del guests[0]
del guests[0]

# Make sure the list is empty. Chapter hadn't covered this specifically. 

guests = []
if (guests):
    print ("The list is not empty")
else:
    print("The guest list is empty.")




