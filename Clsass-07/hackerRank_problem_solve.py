# Hackerank Problem Solve
N = int(input())
listFinal: list[int] = []

for i in range(N):
    inputN = input().split(" ")

    if inputN[0] == "print":
        print(listFinal)
        break

    if len(inputN) == 3:
        if inputN[0] == "insert":
            listFinal.insert(int(inputN[1]), int(inputN[2]))
    elif len(inputN) == 2:
        if inputN[0] == "remove":
            listFinal.remove(int(inputN[1]))
        elif inputN[0] == "append":
            listFinal.append(int(inputN[1]))
    elif len(inputN) == 1:
        if inputN[0] == "sort":
            listFinal.sort()
        elif inputN[0] == "pop":
            listFinal.pop()
        elif inputN[0] == "reverse":
            listFinal.reverse()
