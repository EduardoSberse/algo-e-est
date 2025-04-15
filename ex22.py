palavras = []
quantidade = 0 
palavra = ""

for i in range(6):
    palavras.append(input(f"Digite a {i + 1}° palavra: "))
 


for palavra in palavras:
    if len(palavra) > 5 :
        quantidade += 1 
print (f"A quantiade de palavars com mais de 5 letras é: {quantidade} ")