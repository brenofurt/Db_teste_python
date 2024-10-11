import random

# Gera 10 números aleatórios entre 0 e 100
numeros = [random.randint(0, 100) for _ in range(10)]

# Exibe os números na tela
print("Números gerados:", numeros)

# Identifica o menor e o maior número
menor = min(numeros)
maior = max(numeros)

# Exibe o menor e o maior número
print("Menor número:", menor)
print("Maior número:", maior)
