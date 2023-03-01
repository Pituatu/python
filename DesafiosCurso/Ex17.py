# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor de seno, cosseno e tangente
# desse ângulo:

import math
angulo = float(input("Digite o valor do ângulo: "))
print(f'O seno desse ângulo é igual a {round(math.sin(math.radians(angulo)), 4)}.')
print(f'O cosseno desse ângulo é igual a {round(math.cos(math.radians(angulo)), 4)}.')
print(f'A tangente desse ângulo é igual a {round(math.tan(math.radians(angulo)), 4)}')