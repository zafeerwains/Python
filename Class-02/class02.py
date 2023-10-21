name: str = "Muhammad Zafeer"
print(type(name))
print(name)

# convert any special character into simple character by adding \ sign
message: str = 'His father\'s bussiness is good'
print(message)

# / line  break to next
print("this is a \
good language")


# f string power f"""portal{variable}"""
print(f"""
Student Name = {name}""")

dir(str)
[i for i in dir(str) if "__" not in i]
