print("*********************************")
print("Bem Vindo ao Jogo da Adivinhação!")
print("*********************************")

numero_secreto = 12
chute = input("Digite o seu número:")
chute_int = int(chute)
acertou = numero_secreto == chute_int
chute_maior = chute_int > numero_secreto
chute_menor = chute_int < numero_secreto



print("Você digitou", chute_int)


if(acertou):
    print("Parabéns você acertou!")
else:
    if(chute_maior):
        print("Você errou! Seu número é maior que o número secreto!")
    elif(chute_menor):
        print("Você errou! Seu número é menor que o número secreto!")


print("******************************")
print("Fim do Jogo!")
print("******************************")