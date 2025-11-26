"""
3 -  Crie um programa que leia um arquivo  informado pelo usuário, 
percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, 
mostre uma mensagem de erro.
"""
import os

def ler_arquivo_texto():
    """
    Lê um arquivo de texto informado pelo usuário.
    """
    print("=== LEITOR DE ARQUIVO DE TEXTO ===")
    
    arquivo = input("Digite o nome do arquivo para ler: ").strip()
    
    try:
        # Verifica se o arquivo existe no diretório atual
        if not os.path.exists(arquivo):
            # Tenta encontrar o arquivo no mesmo diretório do script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            arquivo_path = os.path.join(script_dir, arquivo)
            
            if not os.path.exists(arquivo_path):
                raise FileNotFoundError(f"Arquivo '{arquivo}' não encontrado!")
            else:
                arquivo = arquivo_path
        
        # Tenta diferentes codificações
        codificacoes = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        conteudo = None
        
        for encoding in codificacoes:
            try:
                with open(arquivo, 'r', encoding=encoding) as file:
                    linhas = file.readlines()
                    conteudo = linhas
                    encoding_usado = encoding
                    break
            except UnicodeDecodeError:
                continue
        
        if conteudo is None:
            # Última tentativa com tratamento de erro
            with open(arquivo, 'r', encoding='utf-8', errors='ignore') as file:
                conteudo = file.readlines()
                encoding_usado = 'utf-8 (com tratamento de erros)'
        
        print(f"\n📖 CONTEÚDO DO ARQUIVO: {os.path.basename(arquivo)}")
        print(f"🔤 Codificação detectada: {encoding_usado}")
        print("="*50)
        
        numero_linha = 1
        for linha in conteudo:
            # Remove espaços em branco no final e exibe com numeração
            linha_limpa = linha.rstrip()
            print(f"{numero_linha:3d}: {linha_limpa}")
            numero_linha += 1
        
        print("="*50)
        print(f"📊 Total de linhas: {numero_linha - 1}")
        print(f"💾 Caminho completo: {arquivo}")
        
    except FileNotFoundError as e:
        print(f"❌ {e}")
        print("\n💡 Arquivos disponíveis no diretório:")
        try:
            arquivos = os.listdir('.')
            for arq in arquivos:
                if arq.endswith('.txt') or arq.endswith('.csv'):
                    print(f"   - {arq}")
        except:
            print("   (Não foi possível listar os arquivos)")
            
    except PermissionError:
        print("❌ Erro: Permissão negada para ler o arquivo!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

# Executar
if __name__ == "__main__":
    ler_arquivo_texto()