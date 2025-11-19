'''
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
'''

# Calculadora de Desconto
print("=== CALCULADORA DE DESCONTO ===")

try:
    # Entrada de dados
    preco_original = float(input("Digite o preço original do produto: R$ "))
    porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))
    
    # Verifica valores válidos
    if preco_original < 0:
        print("❌ Erro: O preço não pode ser negativo!")
    elif porcentagem_desconto < 0:
        print("❌ Erro: O desconto não pode ser negativo!")
    elif porcentagem_desconto > 100:
        print("❌ Erro: O desconto não pode ser maior que 100%!")
    else:
        # Cálculos
        valor_desconto = preco_original * (porcentagem_desconto / 100)
        preco_final = preco_original - valor_desconto
        
        # Exibe resultados formatados
        print("\n" + "="*40)
        print("💰 RESUMO DO CÁLCULO:")
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto ({porcentagem_desconto}%): R$ {valor_desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
        
        # Mostra economia
        economia = valor_desconto
        print(f"💵 Você economizou: R$ {economia:.2f}")

except ValueError:
    print("❌ Erro: Digite valores numéricos válidos!")