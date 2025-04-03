nota1 = float (input("Insira sua nota: ")) 
nota2 = float (input("Insira sua nota: ")) 
nota3 = float (input("Insira sua nota: ")) 

if (nota1 + nota2 + nota3) / 3 >= 7.0:
    print("Aprovado") 

elif (nota1 + nota2 + nota3) / 3 >= 5:
    print("Recuperação")

else: 
    print("Reprovado")