preco = float (input("Insira o valor de sua compra: ")) 
nome = input("Insira o nome do produto: ") 
quant = float (input("Insira a quantidade do produto: ")) 

if preco * quant >= 100: 
    preco_desc =quant * preco-( preco * quant * 0.05)
    print (f"O valor de sua compra é: R$ {preco_desc}") 
else: 
    print (f"O valor de sua compra é: R$ {preco}")