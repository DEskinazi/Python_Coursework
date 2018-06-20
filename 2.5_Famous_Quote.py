# Using the single apostrophe for adding quotes
famous_quote = '"Wilderness in not a luxury but a necessity of the human spirit."'
message = "Writer Edward Abbey once said, " + famous_quote
print(message)

# Alternate method not in book. Using the escape character \" for adding quotes.
famous_quote = "Wilderness in not a luxury but a necessity of the human spirit."
message = "Writer Edward Abbey once said, " + "\"" + famous_quote + "\""
print(message)