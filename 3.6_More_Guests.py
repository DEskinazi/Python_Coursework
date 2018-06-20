# Using the program in Exercise 3.5, add more guests to the party list using .append and .insert.

guests = ['chuchi', 'morris', 'celia']
print("Please join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")

print("\nI found a bigger dinner table and we can now invite more guests.")

guests.insert(0, 'abraham')
print(guests)

guests.insert(2, 'tio vitali')
print(guests)

guests.append('luba')
print(guests)

# Print a new invitation for each guest.
print("\nPlease join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")
print("Please join me for my party, " + guests[3].title() + ".")
print("Please join me for my party, " + guests[4].title() + ".")
print("Please join me for my party, " + guests[5].title() + ".")




