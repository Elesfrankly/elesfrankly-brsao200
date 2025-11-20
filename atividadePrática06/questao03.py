'''
3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, 
cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma 
mensagem de falha.
'''

import requests

print("=== CONSULTA RÁPIDA DE CEP ===")

cep = input("Digite o CEP: ").replace("-", "").replace(" ", "")

if len(cep) != 8 or not cep.isdigit():
    print("❌ CEP inválido! Use 8 dígitos.")
else:
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        dados = resposta.json()
        
        if 'erro' in dados:
            print("❌ CEP não encontrado!")
        else:
            print(f"\n📍 CEP: {dados['cep']}")
            print(f"🏠 Logradouro: {dados['logradouro']}")
            print(f"🏘️ Bairro: {dados['bairro']}")
            print(f"🏙️ Cidade: {dados['localidade']}")
            print(f"🇧🇷 Estado: {dados['uf']}")
            
    except:
        print("❌ Erro na consulta!")