import random

def jogar():

    imprimeCabecario()
    palavraSecreta = carregaPalavraSecreta() 
    palavraAtual = carregaPalavraAtual(palavraSecreta)
    
    #Variáveis Globais
    tentativas = 0
    perdeuJogo = False
    ganhouJogo = False

    
    def atualizaPalavraAtual(chute):            #Função de validação da palavra criada pelos chutes do jogador com a palavra secreta
        nonlocal palavraAtual                   #Declaração variável global fora do escopo da função
        nonlocal ganhouJogo
        nonlocal tentativas

        if (chute in palavraSecreta):  
            for i in range(len(palavraSecreta)):#Varre todos os caracteres da palavra secreta
                letra = palavraSecreta[i]       #Variável indicando a letra atual no loop de validação.
            
                if (chute == letra):            #Se o chute do jogador existir na palavra secreta guarda essa informação na palavra atual.
                    palavraAtual[i] = chute     #Implementa palavra atual com as letras que o jogador já acertou.
                if(chute == palavraSecreta):    #Se o chute for igual a palavra secreta o jogo acaba
                    palavraAtual = chute
                    ganhouJogo = True
        else:
            tentativas += 1

    def imprimePalavra():                       #Função que imprime a palavra atual no console
        print(palavraAtual)                    

    print(palavraAtual)

    while not perdeuJogo and not ganhouJogo:    #Laço que verifica se o jogo continua ou termina.

        chute = input("Qual letra? ").upper()   #Campo de interação onde o jogador digita uma letra para chutar a resposta, campo tratado para sempre ser maiúsculo.
        chute = chute.strip()
        atualizaPalavraAtual(chute)             #Chamada da função que valida a palavra atual.
        imprimePalavra()                        #Chamada da função que imprime a palavra atual.
        
        if (palavraAtual == palavraSecreta):    #Verifica se o jogador acertou a palavra secreta.
            ganhouJogo = True

        perdeuJogo = tentativas == 6
        ganhouJogo = "_" not in palavraAtual
   
    if (ganhouJogo):
        print("Você ganhou!")
    else:
        print("Você perdeu, deu FORCA!!!")      #Ao sair do laço indica que o jogo acabou.
    input()                                     #Apertar qualquer tecla para sair.


def imprimeCabecario():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregaPalavraSecreta():
    palavras = []
   
    with open("palavras.txt") as arquivo: #Abre o arquivo palavras.txt e joga o conteudo do arquivo na variável "arquivo", chamada da função OPEN pelo WITH.
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    indice = random.randrange(0, len(palavras))
    palavraSecreta = palavras[indice].upper()
    return palavraSecreta

def carregaPalavraAtual(palavraSecreta):
    return ["_" for letra in palavraSecreta]

if __name__ == "__main__":
    jogar()