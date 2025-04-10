idade = int (input("Digite sua idade"))
mem = str (input)("Você é membro do clube") 
acom = str (input)("você está acompanhado de membros?")

if idade >= 18 and mem == "sim": 
    print("sejá bem vindo") 
elif idade < 18: 
    print ("Proibido a entrada de menores") 
elif idade >= 18 and mem == "não" and acom == "não": 
    print("Você deve pagar entrada cheia")
else: 
    idade >= 18 and mem == "não" and acom == "sim"
    print("Você deve pagar meia entrada")