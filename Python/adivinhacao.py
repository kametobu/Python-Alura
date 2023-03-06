import random

def jogar_advinhacao():
    print("=================================")
    print("Bem vindo no jogo de adivinhação!")
    print("=================================")

    pontos = 1000

    print("Qual nível deficudade?")
    print("(1) fácil (2) Médio (3) difícil)")

    nivel = int(input("Defina o nível: "))

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = input("Digite o seu numero: ")

        print("Você digitou ", chute)
        if(int(chute)<1 or int(chute)>100):
            print("Você deve digitar um numero entre 1 e 100")
            continue
        if(int(chute) == numero_secreto):
            print(f"Você acertou!, na {rodada} tentativas")
            break
        elif(int(chute) > numero_secreto):

            print("Você errou!, o seu chute foi maior que o número secreto.")
        elif(int(chute) < numero_secreto):

            print("Você errou!, o seu chute foi menor que o número secreto.")
        pontos -=  abs(int(chute) - numero_secreto)

    print("-----------RESULTADO------------")
    print(f"Numero Secreto {numero_secreto}")
    print(f"Total de pontos: {pontos}")
    print("Fim do jogo")

if __name__ == '__main__':
    jogar_advinhacao()