# Programa para construir a tabuada de um número

# Solicita ao usuário que digite um número
numero = int(input("Digite um número para ver sua tabuada: "))
print() # quebra de linha pra melhorar a visualização
# Loop para calcular e exibir a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
