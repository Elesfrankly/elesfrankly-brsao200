"""
2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, 
que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, 
caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
"""
import csv
import os

def criar_csv():
    """
    Cria um arquivo CSV com dados de pessoas.
    """
    print("=== CRIADOR DE ARQUIVO CSV ===")
    
    try:
        nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.csv): ").strip()
        
        if not nome_arquivo.endswith('.csv'):
            nome_arquivo += '.csv'
        
        # Dados de exemplo
        pessoas = [
            {'nome': 'Ana Silva', 'idade': 25, 'cidade': 'São Paulo'},
            {'nome': 'João Santos', 'idade': 30, 'cidade': 'Rio de Janeiro'},
            {'nome': 'Maria Oliveira', 'idade': 22, 'cidade': 'Belo Horizonte'},
            {'nome': 'Pedro Costa', 'idade': 35, 'cidade': 'Porto Alegre'},
            {'nome': 'Carla Rodrigues', 'idade': 28, 'cidade': 'Salvador'}
        ]
        
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as file:
            campos = ['nome', 'idade', 'cidade']
            escritor = csv.DictWriter(file, fieldnames=campos)
            
            # Escreve o cabeçalho
            escritor.writeheader()
            
            # Escreve os dados
            for pessoa in pessoas:
                escritor.writerow(pessoa)
        
        print(f"\n✅ Arquivo '{nome_arquivo}' criado com sucesso!")
        
        # Mostra o conteúdo criado
        print("\n📋 Conteúdo do arquivo:")
        print("="*40)
        print(f"{'Nome':<20} {'Idade':<10} {'Cidade':<15}")
        print("-" * 40)
        
        for pessoa in pessoas:
            print(f"{pessoa['nome']:<20} {pessoa['idade']:<10} {pessoa['cidade']:<15}")
        
        print(f"\n💾 Arquivo salvo em: {os.path.abspath(nome_arquivo)}")
        
    except PermissionError:
        print("❌ Erro: Permissão negada para criar o arquivo!")
    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")

# Executar
criar_csv()