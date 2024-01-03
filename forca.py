def jogar():

    print("*****************************")
    print("Bem Vindo ao Jogo da Forca!")
    print("*****************************\n")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print("Palavra {}\n".format(letras_acertadas))

    while(not enforcou and not acertou):
        
        chute = input("Qual a letra?\n")
        chute = chute.strip()
        
        index = 0
        
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        
        print(letras_acertadas)
            

            
    


    print("******************************")
    print("Fim do Jogo!")
    print("******************************\n")

if(__name__ == "__main__"):
    jogar()