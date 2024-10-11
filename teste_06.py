# Função para calcular o valor total com desconto
def calcular_total(preco, quantidade):
    if quantidade <= 10:
        total = preco * quantidade
    elif 11 <= quantidade <= 20:
        total = preco * quantidade * 0.90  # 10% de desconto
    elif 21 <= quantidade <= 50:
        total = preco * quantidade * 0.80  # 20% de desconto
    else:
        total = preco * quantidade * 0.75  # 25% de desconto
    return total

# Solicita os dados do produto
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: R$ "))
quantidade_produto = int(input("Digite a quantidade comprada: "))

# Calcula o total a ser pago
valor_total = calcular_total(preco_produto, quantidade_produto)

# Exibe o resultado
print(f"\nProduto comprado: {nome_produto}")
print(f"Valor total a ser pago: R$ {valor_total:.2f}")
