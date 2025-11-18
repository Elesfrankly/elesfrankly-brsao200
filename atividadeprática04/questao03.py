'''
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos 
de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
'''

'''# Verificador de Segurança de Senha
print("=== VERIFICADOR DE SENHA ===")

senha = input("Digite sua senha: ")

# Verifica os critérios
tem_8_caracteres = len(senha) >= 8
tem_numero = any(caractere.isdigit() for caractere in senha)

if tem_8_caracteres and tem_numero:
    print("✅ Senha segura! Atende aos critérios.")
else:
    print("❌ Senha insegura! Verifique:")
    if not tem_8_caracteres:
        print("   - Deve ter pelo menos 8 caracteres")
    if not tem_numero:
        print("   - Deve conter pelo menos um número")'''

while True:
    senha = input("Digite a sua senha:")

    if senha.lower() == "sair":
        print("Programa encererado")
        break

    tem_oito_caracteres = len(senha) >= 8 

    tem_numero = any(caractere.isdigit() for caractere in senha)

    eh_forte = tem_oito_caracteres and tem_numero

    if eh_forte: 
        print("Parabéns. Sua senha é muito forte")
        break
    else:
        print("Que pena. Sua senha está fraca")

    if not tem_oito_caracteres:
        print("A senha tem que ter pelo menos 8 caracteres")   
    if not tem_numero:
        print ("A senha tem que ter pelo menos 1 número")