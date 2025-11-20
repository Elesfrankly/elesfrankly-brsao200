'''1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também 
escolha o tamanho da senha  para criar senhas seguras automaticamente.
'''

import random
import string

print("=== GERADOR EM LOTE ===")

quantidade = int(input("Quantas senhas? "))
tamanho = int(input("Tamanho de cada senha? "))

print("\n🔐 SENHAS GERADAS:")
print("-" * 40)

for i in range(quantidade):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f"{i+1:2d}. {senha}")

print("-" * 40)
print(f"✅ {quantidade} senhas geradas com sucesso!")