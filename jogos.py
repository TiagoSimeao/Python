import forca
import adivinhação


def escolher_jogo():
    print("*********************")
    print("Escolha o seu jogo!")
    print("**********************\n")

    jogo = 0

    while jogo == 1 or 2:

        print("(1) Jogo da Adivinhação (2) Jogo da Forca\n")
        jogo = int(input("Escolha o Jogo:"))

        if(jogo == 1):
            print("Iniciando Jogo da advinhação!")
            adivinhação.jogar()
            

        elif(jogo == 2):
            print("Iniciando Jogo da Forca!")
            forca.jogar()
            
        else:
            print("Você não digitou uma opção válida!")
            continue

if(__name__ == "__main__"):
    escolher_jogo()