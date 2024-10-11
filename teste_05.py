import random

# Opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Solicita a escolha do jogador
jogador = input("Escolha pedra, papel ou tesoura: ").lower()

# Verifica se a escolha do jogador é válida
if jogador not in opcoes:
    print("Escolha inválida! Tente novamente.")
else:
    # Gera a escolha da máquina
    maquina = random.choice(opcoes)
    print("A máquina escolheu:", maquina)

    # Determina o vencedor
    if jogador == maquina:
        print("Empate!")
    elif (jogador == "pedra" and maquina == "tesoura") or \
         (jogador == "papel" and maquina == "pedra") or \
         (jogador == "tesoura" and maquina == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
