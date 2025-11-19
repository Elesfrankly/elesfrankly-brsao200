'''
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """Calcula o valor da gorjeta."""
    return valor_conta * (porcentagem_gorjeta / 100)

# Programa com opções de gorjeta
print("=== CALCULADORA DE GORJETA INTELIGENTE ===")

valor_conta = float(input("Digite o valor da conta: R$ "))

print("\n💡 Sugestões de gorjeta:")
print("1 - 10% (Serviço OK)")
print("2 - 15% (Serviço Bom)")
print("3 - 20% (Serviço Excelente)")
print("4 - Personalizada")

opcao = input("\nEscolha uma opção (1-4): ")

if opcao == "1":
    porcentagem = 10
elif opcao == "2":
    porcentagem = 15
elif opcao == "3":
    porcentagem = 20
elif opcao == "4":
    porcentagem = float(input("Digite a porcentagem desejada: "))
else:
    print("Opção inválida! Usando 15% como padrão.")
    porcentagem = 15

# Cálculos
gorjeta = calcular_gorjeta(valor_conta, porcentagem)
total = valor_conta + gorjeta

# Resultado
print("\n" + "="*40)
print(f"📊 Valor da gorjeta ({porcentagem}%): R$ {gorjeta:.2f}")
print(f"💰 Total a pagar: R$ {total:.2f}")