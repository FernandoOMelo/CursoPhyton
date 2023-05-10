import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
print("(1 - Fácil) (2 - Médio) (3 - Díficil) (4 - Extremo)")
dificuldade = int(input("Selecione o nível do jogo: "))
pontos = 1000

if dificuldade == 1:
    total_tentativas = 10
elif dificuldade == 2:
    total_tentativas = 5
elif dificuldade == 3:
    total_tentativas = 3
elif dificuldade == 4:
    total_tentativas = 1

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um número de 1 à 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    pontos_perdidos = abs(numero_secreto - chute)

    if (acertou):
        print("Parabéns você acertou e fez {} pontos!".format(pontos))
        print("Fim do Jogo!")
        break
    elif(maior):
        print("Você errou, seu chute foi maior que o número sorteado.")
        pontos = pontos - pontos_perdidos

    else:
        print("Você errou seu número é menor do que o número sorteado.")
        pontos = pontos - pontos_perdidos