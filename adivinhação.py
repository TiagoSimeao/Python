def jogar():
    import random 

    print("*********************************")
    print("Bem Vindo ao Jogo da Adivinhação!")
    print("*********************************\n")

    numero_secreto = (random.randrange(1,101))
    fácil = 10
    médio = 5
    difícil = 3
    total_de_tentativas = 0
    pontos = 1000

    while total_de_tentativas == 10 or 5 or 3:
        print("Qual o nivel de dificuldade deseja?")
        dificuldade = input("\n(1) Fácil, (2) médio ou (3) difícil?:")
        
        if(dificuldade == "1"):
            total_de_tentativas = fácil
            
        elif(dificuldade == "2"):
            total_de_tentativas = médio
        
        elif(dificuldade == "3"):
            total_de_tentativas = difícil
            
        elif(dificuldade != "1" != "2" != "3"):
            print("Você não inseriu uma dificuldade válida! Tente novamente!\n")
            continue
        else:
            total_de_tentativas = difícil

        for rodada in range(1,total_de_tentativas + 1):
            print("\n---- Tentativa {} de {}\n". format(rodada, total_de_tentativas))
            chute = input("Digite um número entre 1 e 100:")
            chute_int = int(chute)

            if(chute_int < 1 or chute_int > 100):
                print("O número não está entre 1 e 100! Tente novamente! \n")
                continue

            acertou = numero_secreto == chute_int
            chute_maior = chute_int > numero_secreto
            chute_menor = chute_int < numero_secreto

            print("\nVocê digitou", chute_int, "\n")

            if(acertou):
                print("Parabéns você acertou!\n")
                break
            else:
                if(chute_maior):
                    print("Você errou! Seu número é maior que o número secreto!\n")
                elif(chute_menor):
                    print("Você errou! Seu número é menor que o número secreto!\n")

                pontos_perdidos = abs(numero_secreto - chute_int) 
                pontos = pontos - pontos_perdidos

        if(rodada == total_de_tentativas):
            print("O número secreto era:",numero_secreto)
        
        if(acertou or rodada == total_de_tentativas):
            print("Você fez {} pontos!\n" .format(pontos))

        print("******************************")
        print("Fim do Jogo!")
        print("******************************\n")

        break
if(__name__== "__main__"):    
    jogar()