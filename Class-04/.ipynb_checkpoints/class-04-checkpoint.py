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

