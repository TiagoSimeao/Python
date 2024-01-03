def jogar():

    print("*****************************")
    print("Bem Vindo ao Jogo da Forca!")
    print("*****************************\n")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input("Qual a letra?\n")
        chute = chute.strip()
        
        posição = 1
        
        for letra in palavra_secreta:

            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute,posição))
            posição = posição + 1
        
        print("jogando...")
            

            
    


    print("******************************")
    print("Fim do Jogo!")
    print("******************************\n")

if(__name__ == "__main__"):
    jogar()