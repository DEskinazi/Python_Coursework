# Store a person's name, and include some whitespace at the beginning and end. Use each character combination, "\t" and "\n", at least once.
person="  Ilana  "
print("Ilana")
print("\tIlana")
print("\n" + person.lstrip())
print("\n" + person.rstrip())
print("\n" + person.strip())