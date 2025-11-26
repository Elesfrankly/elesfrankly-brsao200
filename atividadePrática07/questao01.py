"""
1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , 
calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, 
mostre uma mensagem de erro. 
"""
import csv
import os

def analisar_csv():
    """
    Lê um arquivo CSV e calcula média e máximo da coluna tempo_execucao.
    """
    print("=== ANALISADOR DE ARQUIVO CSV ===")
    
    arquivo = input("Digite o nome do arquivo CSV: ").strip()
    
    try:
        # Verifica se o arquivo existe no diretório atual
        if not os.path.exists(arquivo):
            # Tenta encontrar o arquivo no mesmo diretório do script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            arquivo_path = os.path.join(script_dir, arquivo)
            
            if not os.path.exists(arquivo_path):
                raise FileNotFoundError(f"Arquivo '{arquivo}' não encontrado no diretório atual!")
            else:
                arquivo = arquivo_path
        
        tempos = []
        total_linhas = 0
        
        with open(arquivo, 'r', newline='', encoding='utf-8') as file:
            # Tenta detectar o delimitador
            sample = file.read(1024)
            file.seek(0)  # Volta ao início do arquivo
            
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            leitor = csv.DictReader(file, delimiter=delimiter)
            
            # Verifica se a coluna tempo_execucao existe
            if leitor.fieldnames is None or 'tempo_execucao' not in leitor.fieldnames:
                print(f"📋 Colunas disponíveis: {leitor.fieldnames}")
                raise ValueError("Coluna 'tempo_execucao' não encontrada no arquivo!")
            
            print(f"\n📊 Lendo arquivo: {os.path.basename(arquivo)}")
            print(f"📋 Colunas disponíveis: {', '.join(leitor.fieldnames)}")
            print(f"🔍 Delimitador detectado: '{delimiter}'")
            
            for linha in leitor:
                total_linhas += 1
                try:
                    if 'tempo_execucao' in linha and linha['tempo_execucao'].strip():
                        tempo = float(linha['tempo_execucao'])
                        tempos.append(tempo)
                except ValueError:
                    print(f"⚠️  Valor inválido na linha {total_linhas}: '{linha.get('tempo_execucao', 'N/A')}'")
        
        if not tempos:
            print("❌ Nenhum dado válido encontrado na coluna tempo_execucao!")
            return
        
        # Cálculos
        media = sum(tempos) / len(tempos)
        maximo = max(tempos)
        minimo = min(tempos)
        
        # Resultados
        print("\n" + "="*50)
        print("📈 RESULTADOS DA ANÁLISE:")
        print("="*50)
        print(f"📊 Total de linhas processadas: {total_linhas}")
        print(f"📊 Registros válidos na coluna tempo_execucao: {len(tempos)}")
        print(f"📊 Média do tempo de execução: {media:.2f} segundos")
        print(f"📈 Máximo tempo de execução: {maximo:.2f} segundos")
        print(f"📉 Mínimo tempo de execução: {minimo:.2f} segundos")
        
    except FileNotFoundError as e:
        print(f"❌ {e}")
        print("💡 Certifique-se de que o arquivo está no mesmo diretório do script.")
    except PermissionError:
        print("❌ Erro: Permissão negada para ler o arquivo!")
    except ValueError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

# Executar
if __name__ == "__main__":
    analisar_csv()