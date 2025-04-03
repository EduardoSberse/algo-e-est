nome = input ("Insira seu nome: ") 
idade = int(input("insira sua idade: ")) 
turma = input ("Insira sua turma: ") 

if idade >= 6:

    print (f"Aluno cadastrado com sucesso: {nome}, {idade} anos e turma {turma}") 
else:
    print("Idade invalida")
