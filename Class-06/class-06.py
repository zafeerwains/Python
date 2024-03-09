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
s = "qwertyuiopasdfghjklzxcvbnm"
obj = {}
# l = []
for i in s:
    if i not in obj:
        obj[i] = 0
    obj[i] += 1
values = sorted(obj.items())
val = sorted(values, key=lambda x: x[-1], reverse=True)[:3]
print(val[0][0], val[0][1])
print(val[1][0], val[1][1])
print(val[2][0], val[2][1])

