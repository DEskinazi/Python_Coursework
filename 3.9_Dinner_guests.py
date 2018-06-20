# Using the program in Exercise 3.7, Use len() to print a message indicating how many guests will come to the party.
guests = ['chuchi', 'morris', 'celia']
print("Please join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")

print("\nI found a bigger dinner table and we can now invite more guests.")

guests.insert(0, 'abraham')

guests.insert(2, 'tio vitali')

guests.append('luba')

# Print a new invitation for each guest.
print("\nPlease join me for my party, " + guests[0].title() + ".")
print("Please join me for my party, " + guests[1].title() + ".")
print("Please join me for my party, " + guests[2].title() + ".")
print("Please join me for my party, " + guests[3].title() + ".")
print("Please join me for my party, " + guests[4].title() + ".")
print("Please join me for my party, " + guests[5].title() + ".")
# Print the number of guests invited to dinner. 
print(len(guests))


# Name the number of guests invited in a sentence.
print("\nWe are having " + str(len(guests)) + " guests to dinner.")
