# practice a problem random
# string: str = "abbcacaea"
# n: int = 3
# split_strings:list[str]=[string[i:i+n] for i in range(0,len(string),n)];
#     for i in range(0,len(split_strings)):
#         sub_string=split_strings[i]
#         output=""
#         for i in range(0,len(sub_string)):
#             output=sub_string[0]
#             if sub_string[i] not in output :
#                 output+=sub_string[i]
#         print(output)

# Replace "your_input_string" with the actual string you want to process
# s = "qwertyuiopasdfghjklzxcvbnm"
# obj = {}
# # l = []
# for i in s:
#     if i not in obj:
#         obj[i] = 0
#     obj[i] += 1
# values = sorted(obj.items())
# val = sorted(values, key=lambda x: x[-1], reverse=True)[:3]
# print(val[0][0], val[0][1])
# print(val[1][0], val[1][1])
# print(val[2][0], val[2][1])


# Chapter 4 Questions strting from here
# Problem 4-1
pizzas: list[str] = ["Supremen", "corn", "Kabab"]
for pizza in pizzas:
    print(f"The name of the pizza , {pizza}")
print("The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!")

# Problem 4-2
Animals: list[str] = ["cat", "lion", "cheetah"]
for animal in Animals:
    print(f"I like {animal}")
print("Any of these animals would make a great pet!")
