# Problem 1-2
print("Hello World!")

# Problem 2-1
message: str = "Message Is This that we are trying to Cover the Pyhton by full attention"
print(message)

# Problem 2-2
message = "New Message is that we are trying to Cover the Pyhton by full attention"
print(message)

# Problem 2-3
personName: str = "Eric"
message = f"Hello {personName}, would you like to learn some Python today?"
print(message)

# Problem 2-4
print(personName.upper())
print(personName.lower())
print(personName.title())

# Problem 2-5
quoteText: str = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(quoteText)

# Problem 2-6
famous_person: str = "Albert Einstein"
message = f'''{famous_person}
    once said, “A person who never made a mistake never tried anything new.”'''

# Problem 2-7
famousPerson: str = "                      \t \n  Albert Einstein                    "
print(famousPerson)
print(repr(famousPerson.lstrip()))
print(repr(famousPerson.rstrip()))
print(repr(famousPerson.strip()))

# Problem 2-8
file_name: str = "python_notes.txt"
print(file_name.removesuffix(".txt"))
