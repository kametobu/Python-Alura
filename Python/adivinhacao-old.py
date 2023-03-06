print("=================================")
print("Bem vindo no jogo de adivinhação!")
print("=================================")

numero_secreto = 42
acertou = True
errou = 0

while acertou and errou < 3:
    errou+=1
    print(f"Tentativa {errou} de 3")
    chute = input("Digite o seu numero: ")

    print("Você digitou ", chute)

    if(int(chute) == numero_secreto):
        print(f"Você acertou!, na {errou} tentativas")
        acertou = False
    elif(int(chute) > numero_secreto):
        print("Você errou!, o seu chute foi maior que o número secreto.")
    elif(int(chute) < numero_secreto):
        print("Você errou!, o seu chute foi menor que o número secreto.")

print("Fim do jogo")