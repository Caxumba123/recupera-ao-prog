numero = int(input("Digite um numero maior que 100: "))
while True:
    if numero % 7 == 0 and numero % 3 == 0:
        print(f"O numero é {numero}!")
        break
    numero = numero + 1