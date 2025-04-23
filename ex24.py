numeros = []

for i in range(5):
    numero = int(input(f"Digite um numero: "))
    numeros.append(numero)

maior = numeros[0]
menor = numeros[0]

for i in range(1, 5):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
