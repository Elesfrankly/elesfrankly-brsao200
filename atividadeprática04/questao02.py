'''
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
'''
# Média da Turma (Simples)
n = int(input("Quantos alunos? "))
soma = 0

for i in range(n):
    soma += float(input(f"Nota {i+1}: "))

media = soma / n
print(f"Média: {media:.2f}")

if media >= 7: print("Turma Aprovada")
elif media >= 5: print("turma de Recuperação")
else: print("Turma Reprovada")
