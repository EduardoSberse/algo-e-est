nomes = []

for i in range(4):
    nomes.append(input("Insira um nome: "))

for nome in nomes:
    palinom = True
    for i in range(len(nome)):
        if nome[i] != nome[-(i + 1)]:
            palinom = False
    if palinom:
        print(nome, "é um palindromo")
