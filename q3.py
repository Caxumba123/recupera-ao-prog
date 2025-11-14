list_A = [1, 2, 3, 4, 5]
list_B = [4, 5, 6, 7, 8]

comuns = []

for num in list_A:
    if num in list_B:
        comuns.append(num)

print(comuns)
