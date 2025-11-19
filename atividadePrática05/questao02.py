'''
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, 
responda “Sim”, se o resultado for False, responda “Não”.
'''

def eh_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    """
    texto_limpo = ''.join(caractere.lower() for caractere in texto if caractere.isalnum())
    return texto_limpo == texto_limpo[::-1]

# Programa principal
print("=== VERIFICADOR DE PALÍNDROMOS ===")

while True:
    entrada = input("\nDigite uma palavra ou frase (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        print("Programa encerrado!")
        break
    
    resultado = eh_palindromo(entrada)
    
    print(f"\nTexto original: '{entrada}'")
    if resultado:
        print("✅ Resultado: Sim - É um palíndromo!")
    else:
        print("❌ Resultado: Não - Não é um palíndromo")