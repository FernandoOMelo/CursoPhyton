def jogar():
    #Cabeçario aplicativo
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    #Variáveis Globais
    tentativas = 0
    palavraSecreta = "banana"
    palavraAtual = ["_" for letra in palavraSecreta]
    perdeuJogo = False
    ganhouJogo = False

    
    def atualizaPalavraAtual(chute):            #Função de validação da palavra criada pelos chutes do jogador com a palavra secreta
        nonlocal palavraAtual                   #Declaração variável global fora do escopo da função
        nonlocal ganhouJogo
        nonlocal tentativas

        if (chute in palavraSecreta):  
            for i in range(len(palavraSecreta)):    #Varre todos os caracteres da palavra secreta
                letra = palavraSecreta[i]           #Variável indicando a letra atual no loop de validação.
            
                if (chute == letra):                #Se o chute do jogador existir na palavra secreta guarda essa informação na palavra atual.
                    palavraAtual[i] = chute         #Implementa palavra atual com as letras que o jogador já acertou.
                if(chute == palavraSecreta):        #Se o chute for igual a palavra secreta o jogo acaba
                    palavraAtual = chute
                    ganhouJogo = True
        else:
            tentativas += 1



    def imprimePalavra():                       #Função que imprime a palavra atual no console
        print(palavraAtual)                     #Tratamento para a palavra atual sempre começar com a letra maiúscula.

    print(palavraAtual)

    while not perdeuJogo and not ganhouJogo:    #Laço que verifica se o jogo continua ou termina.

        chute = input("Qual letra? ").lower()   #Campo de interação onde o jogador digita uma letra para chutar a resposta, campo tratado para sempre ser minúsculo.
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
        print("Você perdeu, deu FORCA!!!")                    #Ao sair do laço indica que o jogo acabou.
    input()                                     #Apertar qualquer tecla para sair.

if __name__ == "__main__":
    jogar()
