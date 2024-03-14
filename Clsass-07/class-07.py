# Problem 4-10
pizzas: list[str] = ["Supremen", "corn", "Kabab","Fajita","special","malai bote"]
print(f"The first three items in the list are:")
for pizza in pizzas[0:4]:
    print(pizza)
print(f"The middle three items in the list are:")
for pizza in pizzas[int(len(pizzas)/2):(len(pizzas)//2)+4]:
    print(pizza)
print(f"The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza)

# Problem 4-11
friend_pizzas:list[str]=pizzas.copy()
pizzas.append("smoky")
friend_pizzas.append("chessy sea")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My Fiend favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# Problem 4-12

