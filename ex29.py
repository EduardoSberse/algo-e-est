valores = []

for i in range(4):
    valor = int(input(f"Digite o {i+1} valor: "))
    valores.append(valor)

multiplicador = int(input("Digite um número para multiplicar os outros: "))



for valor in valores:
    print(valor * multiplicador)
