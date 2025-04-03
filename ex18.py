
sal = float(input("Insira seu salário:")) 
extra = int (input("insira a quantidade de horas extras trabalhadas:")) 
valor = float(input("insira o valor por hora de trabalho:")) 

salariomes = extra * valor + sal 
print(f"Seu salario foi: {salariomes}") # o "f" deixa usar variável no print 