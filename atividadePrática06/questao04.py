'''
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, 
máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, 
retorne uma mensagem de erro.
'''

import requests

def cotacao_rapida(moeda):
    """
    Consulta rápida de cotação.
    """
    moeda = moeda.upper()
    
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()
        
        cotacao = dados[f"{moeda}BRL"]
        
        print(f"\n💰 {moeda}/BRL:")
        print(f"💵 Atual: R$ {float(cotacao['bid']):.2f}")
        print(f"📈 Máxima: R$ {float(cotacao['high']):.2f}")
        print(f"📉 Mínima: R$ {float(cotacao['low']):.2f}")
        print(f"📊 Variação: {cotacao['pctChange']}%")
        
    except:
        print("❌ Erro na consulta!")

# Exemplo de uso
cotacao_rapida("USD")