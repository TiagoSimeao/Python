print("*********************")
print("Escolha o seu jogo!")
print("**********************\n")

print("(1) Jogo da Adivinhação (2) Jogo da Forca\n")
jogo = int(input("Escolha o Jogo:"))


if(jogo == 1):
    print("Iniciando Jogo da advinhação!")

elif(jogo == 2):
    print("Iniciando Jogo da Forca!")

else:
    print("Você não digitou uma opção válida!")