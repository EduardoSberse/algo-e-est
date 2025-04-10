numeros = []
soma = 0 
for i in range(1,11):
    numero = int(input(f"Digite o {i}° número"))
    numeros.append(numero)

print(numeros) 

for numero in numeros:
    soma += numero  
print (f"A soma foi: {soma} ")
