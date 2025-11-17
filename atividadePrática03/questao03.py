'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Conversor de Temperatura
print("=" * 50)
print("        CONVERSOR DE TEMPERATURA")
print("=" * 50)

temp = float(input("Digite a temperatura: "))
origem = input("De (C/F/K): ").upper()
destino = input("Para (C/F/K): ").upper()

if origem == "C" and destino == "F":
    resultado = (temp * 9/5) + 32
    print(f"{resultado:.1f}°F")
elif origem == "C" and destino == "K":
    resultado = temp + 273.15
    print(f"{resultado:.1f}K")
elif origem == "F" and destino == "C":
    resultado = (temp - 32) * 5/9
    print(f"{resultado:.1f}°C")
elif origem == "F" and destino == "K":
    resultado = (temp - 32) * 5/9 + 273.15
    print(f"{resultado:.1f}K")
elif origem == "K" and destino == "C":
    resultado = temp - 273.15
    print(f"{resultado:.1f}°C")
elif origem == "K" and destino == "F":
    resultado = (temp - 273.15) * 9/5 + 32
    print(f"{resultado:.1f}°F")
else:
    print("Conversão não suportada!")

