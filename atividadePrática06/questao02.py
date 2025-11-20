'''
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, 
e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
'''

import requests

print("=== BUSCADOR SIMPLES DE USUÁRIOS ===")

try:
    resposta = requests.get('https://randomuser.me/api/')
    resposta.raise_for_status()
    
    dados = resposta.json()
    usuario = dados['results'][0]
    
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    print(f"\n👤 Nome: {nome}")
    print(f"📧 E-mail: {email}")
    print(f"🌎 País: {pais}")
    
except requests.exceptions.RequestException:
    print("❌ Falha na conexão com a API!")
except Exception as e:
    print(f"❌ Erro: {e}")