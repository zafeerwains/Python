# Problem 3-1
names: list[str] = ["Ali", "Akbar", "Abdullah", "Alam"]
print(*names)

# Problem 3-2
print(f"Welcome To the Python Mr.{names[0]}, You can do it .")
print(f"Welcome To the Python Mr.{names[1]}, You can do it .")
print(f"Welcome To the Python Mr.{names[2]}, You can do it .")
print(f"Welcome To the Python Mr.{names[3]}, You can do it .")

# Problem 3-3
transports: list[str] = ["Car", "Bike", "Plane", "Ship"]
messages: list[str] = ["I want to drive super", "I want to Drive a Heavy ",
                       "I want to fly a fighter jet", "I want to sail a "]
print(f'{messages[0]} {transports[0]}.')
print(f'{messages[1]} {transports[1]}.')
print(f'{messages[2]} {transports[2]}.')
print(f'{messages[3]} {transports[3]}.')

# Problem 3-4
guests_list: list[str] = ["Ali", "Akbar", "Azam"]
print(
    f"{guests_list[0]}, You rae invited to join the Dinner Party at my House")
print(
    f"{guests_list[1]}, You rae invited to join the Dinner Party at my House")
print(
    f"{guests_list[2]}, You rae invited to join the Dinner Party at my House")

# Problem 3-5
print(guests_list)
print(
    f"{guests_list[1]} , are now removed from the list because he is no longer available")
newGuest = input("Enter the new guest Who is now available => ")
guests_list[1] = newGuest
print(guests_list)

# Problem 3-6
print("I have Found a Bigger Table so Inviting more guests")
print("Old guests=>", guests_list)
guests_list.insert(0, "Prince")
print("Adding on start, guests=>", guests_list)
guests_list.insert(len(guests_list) // 2, "Prince")
print("Adding on Middle , guests=>", guests_list)
guests_list.append("Tahir")
print("Adding on end Using Append() , guests=>", guests_list)

# Problem 3-7
print("I can invite only two people for dinner")
for i in range(2, len(guests_list)):
    print(f"{guests_list.pop()} I am sorry i can't invite you now")
print(guests_list)
del guests_list

