import random 

print("*********************************")
print("Bem Vindo ao Jogo da Adivinhação!")
print("*********************************")

numero_secreto = (random.randrange(1,101))
total_de_tentativas = 10


for rodada in range(1,total_de_tentativas + 1):
    print("---- Tentativa {} de {}". format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100:")
    chute_int = int(chute)

    if(chute_int < 1 or chute_int > 100):
        print("O número não está entre 1 e 100!")
        continue

    acertou = numero_secreto == chute_int
    chute_maior = chute_int > numero_secreto
    chute_menor = chute_int < numero_secreto

    print("Você digitou", chute_int)

    if(acertou):
        print("Parabéns você acertou!")
        break
    else:
        if(chute_maior):
            print("Você errou! Seu número é maior que o número secreto!")
        elif(chute_menor):
            print("Você errou! Seu número é menor que o número secreto!")


print("******************************")
print("Fim do Jogo!")
print("******************************")