minhas_notas = [8.5, 4.0, 10.0, 7.5, 6.0, 9.0]
soma = 0
cont = 0
for nota in minhas_notas:
    if nota >= 7.0:
        cont += 1

media = soma / len(minhas_notas)
print(f"A media é {media}")
print(f"A quantidade de notas boas é {cont}")