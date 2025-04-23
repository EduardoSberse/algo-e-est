numeros = []
pares = []
impares = []

for i in range(8):
    numero = int(input(f"Digite o {i+1} número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números ímpares:", impares)
