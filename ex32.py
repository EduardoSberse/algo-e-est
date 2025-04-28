base = int(input("Digite um numero desejado:")) 
inicio = int (input("Digite o inicio desejado:")) 
fim = int (input("Digite o fim desejado:")) 
def tabuada_personalizada(base, inicio, fim): 
     print (f"tabuada do {base} de {inicio} a {fim}:") 
     for j in range (inicio, fim + 1 ): 
         print (f"{base} x {j} = {base * j}") 
        
# #uso
tabuada_personalizada ( base, inicio , fim) 
