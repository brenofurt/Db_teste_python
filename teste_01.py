# Programa para ler números até que o usuário digite 10

# Inicia um loop infinito
while True:
    # Solicita ao usuário que digite um número
    numero = int(input("Digite um número (ou 10 para sair): "))
    
    # Verifica se o número digitado é 10
    if numero == 10:
        print("Você digitou 10. Saindo...")
        break  # Encerra o loop se o número for 10
