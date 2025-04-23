nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1} nome: ")
    nomes.append(nome)

nomes.sort()

print("Nomes em ordem são:")
print(nomes)
