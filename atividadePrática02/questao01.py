'''1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. 
Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, 
arredondando para duas casas decimais.'''
real = 100.00
taxaDolar = 5.20
taxaEuro = 6.15

dolar = real * taxaDolar
euro = real * taxaEuro

print("Tenho","R$",real)
print("Em dolar tenho: $",dolar)
print("Em Euro tenho: €",euro)
