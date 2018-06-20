# Using the program from Exercise 3.4, send out new invitations after learning someone can't make it. Add a new guest in their place.
guests = ['chuchi', 'morris', 'santiago']
print("Please join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")

# One person on the list can't make it.

print("I just learned " + guests[2].title() + " can't make it to the party, so we'll have room for one more.")

# Add a new person, replacing the name of the person who can't make it with the new guest.

del guests[2]
guests.append('celia')

# Reprint the invitations to the party.

print("Please join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")
