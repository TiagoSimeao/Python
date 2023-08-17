print("*********************************")
print("Bem Vindo ao Jogo da Adivinhação!")
print("*********************************")

numero_secreto = 12
chute = input("Digite o seu numero:")
chute_int = int(chute)

print("/////////////////////////")
print("Você digitou", chute_int)
print("/////////////////////////")

if(numero_secreto == chute_int):
    print("Parabéns você acertou!")
else:
    print("Você errou!")

print("///////////////////////////")
print("Fim do Jogo!")
print("///////////////////////////")