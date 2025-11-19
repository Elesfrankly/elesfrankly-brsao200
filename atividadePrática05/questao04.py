'''
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
'''

from datetime import datetime

def calcular_dias_vivos(dia, mes, ano):
    """
    Calcula quantos dias uma pessoa está viva.
    """
    data_nascimento = datetime(ano, mes, dia)
    data_atual = datetime.now()
    
    if data_nascimento > data_atual:
        return None, "Data de nascimento no futuro!"
    
    diferenca = data_atual - data_nascimento
    return diferenca.days, None

def formatar_tempo(dias):
    """
    Formata o tempo em anos, meses e dias.
    """
    anos = dias // 365
    meses = (dias % 365) // 30
    dias_restantes = (dias % 365) % 30
    return anos, meses, dias_restantes

# Programa principal
print("=== CALCULADORA DE TEMPO DE VIDA ===")

try:
    print("\nDigite sua data de nascimento:")
    dia = int(input("Dia (1-31): "))
    mes = int(input("Mês (1-12): "))
    ano = int(input("Ano (ex: 1990): "))
    
    dias_vivo, erro = calcular_dias_vivos(dia, mes, ano)
    
    if erro:
        print(f"❌ {erro}")
    else:
        anos, meses, dias_rest = formatar_tempo(dias_vivo)
        
        print("\n" + "="*45)
        print(f"🎂 Data de nascimento: {dia:02d}/{mes:02d}/{ano}")
        print(f"📅 Hoje: {datetime.now().strftime('%d/%m/%Y')}")
        print(f"⏰ Dias vividos: {dias_vivo:,}".replace(',', '.'))
        print(f"\n📊 Isso equivale a:")
        print(f"   {anos} anos, {meses} meses e {dias_rest} dias")
        
        # Estatísticas interessantes
        print(f"\n🌟 Curiosidades:")
        print(f"   Você já viveu {dias_vivo // 7} semanas")
        print(f"   Você já viveu {dias_vivo * 24:,} horas".replace(',', '.'))
        print(f"   Seu próximo aniversário de 1 milhão de horas será em aproximadamente {((1000000 - (dias_vivo * 24)) // 24):,} dias".replace(',', '.'))

except ValueError:
    print("❌ Por favor, digite números válidos para a data!")