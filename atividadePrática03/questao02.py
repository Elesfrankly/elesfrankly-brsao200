'''2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"'''

# Calculadora de IMC
print("=" * 50)
print("          CALCULADORA DE IMC")
print("=" * 50)

# Solicita os dados do usuário
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (metros): "))

# Verifica se os valores são positivos
if peso <= 0 or altura <= 0:
        print("❌ Erro: Peso e altura devem ser valores positivos!")
else:
    # Calcula o IMC
    imc = peso / (altura ** 2)

# Classifica o IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

# Exibe os resultados
    print("-" * 50)
    print("RESULTADOS:")
    print(f"• Peso: {peso} kg")
    print(f"• Altura: {altura} m")
    print(f"• IMC: {imc:.2f}")
    print(f"• Classificação: {classificacao}")