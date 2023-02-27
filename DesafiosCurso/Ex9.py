# Crie um programa que leia quantos reais
# uma pessoa tem na carteira e quantos
# dólares ela pode comprar.
# Considere 1 Dóllar = 5.20 Reais.
# Considere 1 Euro = 5.52 Reais.
import math

dinheiro = float(input("Digite quantos reais você possui na carteira: "))
print(f'Com {dinheiro} reais é possível comprar {round((dinheiro/5.20), 2)} dólares. ')
print(f'Com {dinheiro} reais é possível comprar {round((dinheiro/5.52), 2)} euros. ')