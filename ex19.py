idade = int(input("Digite sua idade")) 
genero = input("Digite seu gênero")  
atl = str (input ("você é atleta ? som ou não")) 

if idade >= 15 and idade <= 21 and genero == "feminino": 
    print("Maquiagem e moda")
elif idade >= 15 and idade <= 32 and genero == "masculino" and atl == "sim": 
    print("Artigos esportivos")
elif idade >= 15 and idade <= 21 and genero == "masculino" and atl == "não":
    print("Videogames") 
elif idade >= 21 and idade <= 32 and genero == "masculino" and atl == "não": 
    print ("Livros, jardinagem e eletrodomesticos")
elif idade <= 15: 
    print ("artigos infantís")
else: 
    idade >= 22 and idade <= 35 and genero == "feminino"
    print("Artigos esportivos e itens de casa") 

    
    