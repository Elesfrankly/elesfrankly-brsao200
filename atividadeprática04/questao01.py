'''
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
'''

# Calculadora Básica
print("=== CALCULADORA ===")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nOperações disponíveis:")
print("+ : Soma")
print("- : Subtração") 
print("* : Multiplicação")
print("/ : Divisão")

operacao = input("\nDigite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"\n{num1} + {num2} = {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"\n{num1} - {num2} = {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"\n{num1} * {num2} = {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"\n{num1} / {num2} = {resultado}")
    else:
        print("\nErro: Divisão por zero!")
else:
    print("\nOperação inválida!")