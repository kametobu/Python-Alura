from forca import jogar_forca
from adivinhacao import jogar_advinhacao

def escolha_jogo():
    print("=================================")
    print("Escolha o jogo!")
    print("=================================")
    
    
    print("(1) Forca (2) advinhação")
    jogo = int(input("Qual o jogo: "))
    if(jogo == 1):
        jogar_forca()
    elif(jogo == 2):
        jogar_advinhacao()

if __name__ == "__main__":
    escolha_jogo()
