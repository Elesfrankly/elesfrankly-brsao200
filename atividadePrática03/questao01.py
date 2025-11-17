'''1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).'''

# Classificador de Idade
print("=" * 40)
print("    CLASSIFICADOR DE IDADE")
print("=" * 40)

# Solicita a idade do usuário
idade = int(input("Informe a sua idade: "))

print("=" * 50)
if idade < 0:
    print("Idade inválida! Por favor, digite uma idade positiva.")
elif idade <= 12:
    print("Classificação: Criança (0-12 anos)")
elif idade <= 17:
    print("Classificação: Adolescente (13-17 anos)")
elif idade <= 59:
    print("Classificação: Adulto (18-59 anos)")
else:
    print("Classificação: Idoso (60 anos ou mais)")
print("=" * 50)