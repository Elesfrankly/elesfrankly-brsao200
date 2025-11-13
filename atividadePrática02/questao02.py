'''2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. 
Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, 
exibindo todos os detalhes.'''
nomeproduto = "Camiseta"
preco = 50.00
porcentagem = 20

valor_desconto = preco * (porcentagem / 100)
preco_final = preco - valor_desconto

print("############Valor com Desconto###################")
print("Valor com desconto do produto R$: ",preco_final)
print("##################################################")