notas = []
soma = 0

for i in range(5):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)
    soma += nota

media = soma / 5
print(f"A média das notas é: {media}")
