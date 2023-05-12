import random #Importa biblioteca Random necessária para gerar um número aleatório                                               

#Declaração de variáveis globais
perdeuJogo = False                                          
ganhouJogo = False
tentativas = 0

def jogar():                                                    #Função principal que é executada enquando o jogo roda.
    #Importação de variáveis globais
    global perdeuJogo
    global ganhouJogo
    global tentativas

    imprimeCabecario()
    palavraSecreta = carregaPalavraSecreta() 
    palavraAtual = carregaPalavraAtual(palavraSecreta)
    print(palavraAtual)

    while not perdeuJogo and not ganhouJogo: #Laço que verifica se o jogo continua ou termina.
        verificaFimDeJogo(palavraSecreta, palavraAtual)
        loopJogador(palavraSecreta, palavraAtual)

    fimDeJogo(ganhouJogo, palavraSecreta)
    input() #Aperte qualquer tecla para continuar

def imprimeCabecario():                                         #Função que imprime as primeiras linhas do jogo.
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregaPalavraSecreta():                                    #Função que importa a palavra secreta do arquivo de texto.
    palavras = []
   
    with open("palavras.txt") as arquivo: #Abre o arquivo palavras.txt e joga o conteudo do arquivo na variável "arquivo", chamada da função OPEN pelo WITH.
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    indice = random.randrange(0, len(palavras))
    palavraSecreta = palavras[indice].upper()
    return palavraSecreta

def carregaPalavraAtual(palavraSecreta):                        #Função que inicia a palavra atual com o mesmo números de caracteres da palavra secreta.
    return ["_" for letra in palavraSecreta]

def atualizaPalavraAtual(palavraSecreta, chute, palavraAtual):  #Função de validação da palavra criada pelos chutes do jogador com a palavra secreta
    global ganhouJogo
    global tentativas

    if (chute in palavraSecreta):  
        for i in range(len(palavraSecreta)):#Varre todos os caracteres da palavra secreta
            letra = palavraSecreta[i]       #Variável indicando a letra atual no loop de validação.
            
            if (chute == letra):            #Se o chute do jogador existir na palavra secreta guarda essa informação na palavra atual.
                palavraAtual[i] = chute     #Implementa palavra atual com as letras que o jogador já acertou.
            if(chute == palavraSecreta):    #Se o chute for igual a palavra secreta o jogo acaba
                palavraAtual[i] = letra 

    else:
        tentativas += 1
        desenhaForca(tentativas)
    
    return palavraAtual
    
def verificaFimDeJogo(palavraAtual, palavraSecreta):            #Função que monitora se o jogo já acabou.
    global ganhouJogo
    if (palavraAtual == palavraSecreta):    #Verifica se o jogador acertou a palavra secreta.
        ganhouJogo = True

def imprimePalavra(palavraAtual):                               #Função que imprime a palavra atual no console
    print(palavraAtual)   

def fimDeJogo(ganhouJogo, palavraSecreta):                      #Função que imprime resultado da partida.
    if (ganhouJogo):
        imprimeVenceu()
    else:
        print(palavraSecreta)
        imprimePerdeu(palavraSecreta)

def loopJogador(palavraSecreta, palavraAtual):                  #Função do loop de interação com o jogador.
        global perdeuJogo
        global ganhouJogo
        
        chute = input("Qual letra? ").upper()   #Campo de interação onde o jogador digita uma letra para chutar a resposta, campo tratado para sempre ser maiúsculo.
        chute = chute.strip()
        imprimePalavra(atualizaPalavraAtual(palavraSecreta, chute, palavraAtual))
        perdeuJogo = tentativas == 7
        ganhouJogo = "_" not in palavraAtual

def imprimePerdeu(palavraSecreta):                              #Função que imprime a mensagem do perdedor.
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")    

def imprimeVenceu():                                            #Função que imprime a palavra do vencedor.
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenhaForca(tentativas):                                   #Função que desenha a forca a cada erro.
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()