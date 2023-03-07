# Crie um programa que leia um número real e
# mostre sua parte inteira.
import math
numero = float(input('Digite o número: '))
print(f'a parte inteira do número é \033[1;31m{math.trunc(numero)}\033[m.')