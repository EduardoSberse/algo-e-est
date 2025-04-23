num = 11
palpites = []
palpite = 0

while palpite != num:
    palpite = int(input("Acerte o número que está entre 1 e 20: "))
    palpites.append(palpite)
    if palpite != num:
        print("Tente novamente.")
    else:
        print("Você acertou :)")

print("Seus palpites foram:", palpites)
