# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = int(input('Digite o ângulo que você deseja analisar: '))
print(f'O seno de {angulo} é igual a {round(math.sin(math.radians(angulo)), 2)}')
print(f'O cosseno de {angulo} é igual a {round(math.cos(math.radians(angulo)), 2)}')
print(f'A tangente de {angulo} é igual a {round((math.tan(math.radians(angulo))), 2)}')