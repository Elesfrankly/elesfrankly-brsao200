"""
4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, 
idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, 
caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
"""
import json
import os

def gerenciar_json():
    """
    Gerencia arquivos JSON - escreve e lê dados.
    """
    print("=== GERENCIADOR DE ARQUIVOS JSON ===")
    
    try:
        # Dados para salvar
        pessoas = [
            {'nome': 'Ana Silva', 'idade': 25, 'cidade': 'São Paulo'},
            {'nome': 'João Santos', 'idade': 30, 'cidade': 'Rio de Janeiro'},
            {'nome': 'Maria Oliveira', 'idade': 22, 'cidade': 'Belo Horizonte'},
            {'nome': 'Pedro Costa', 'idade': 35, 'cidade': 'Recife'},
            {'nome': 'Carla Rodrigues', 'idade': 28, 'cidade': 'Salvador'}
        ]
        
        nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ").strip()
        
        if not nome_arquivo.endswith('.json'):
            nome_arquivo += '.json'
        
        # 1. ESCREVER no arquivo JSON
        print(f"\n💾 Salvando dados em '{nome_arquivo}'...")
        
        with open(nome_arquivo, 'w', encoding='utf-8') as file:
            json.dump(pessoas, file, indent=4, ensure_ascii=False)
        
        print("✅ Dados salvos com sucesso!")
        
        # 2. LER o arquivo JSON
        print(f"\n📖 Lendo dados de '{nome_arquivo}'...")
        
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            dados_lidos = json.load(file)
        
        # Exibir dados lidos
        print("\n" + "="*50)
        print("👥 DADOS LIDOS DO ARQUIVO JSON:")
        print("="*50)
        
        for i, pessoa in enumerate(dados_lidos, 1):
            print(f"\n👤 Pessoa {i}:")
            print(f"   📛 Nome: {pessoa['nome']}")
            print(f"   🎂 Idade: {pessoa['idade']} anos")
            print(f"   🏙️ Cidade: {pessoa['cidade']}")
        
        print(f"\n📊 Total de registros: {len(dados_lidos)}")
        print(f"💾 Arquivo: {os.path.abspath(nome_arquivo)}")
        
        # Mostrar estrutura JSON
        print(f"\n📋 Estrutura do arquivo JSON:")
        print(json.dumps(dados_lidos[0], indent=2, ensure_ascii=False))
        
    except PermissionError:
        print("❌ Erro: Permissão negada para acessar o arquivo!")
    except Exception as e:
        print(f"❌ Erro: {e}")

# Executar
gerenciar_json()