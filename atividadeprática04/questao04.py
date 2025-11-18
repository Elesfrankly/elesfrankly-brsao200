'''
4 - Criar um código que serve para analisar números digitados pelo usuário, 
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
'''

# Analisador de Números Pares e Ímpares
print("=== ANALISADOR DE NÚMEROS ===")

quantidade = int(input("Quantos números deseja analisar? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        print(f"  {numero} é PAR")
        pares += 1
    else:
        print(f"  {numero} é ÍMPAR")
        impares += 1

print("\n" + "="*30)
print("RESULTADO FINAL:")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
print(f"Total de números analisados: {quantidade}")
