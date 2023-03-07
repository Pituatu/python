# Crie um programa que leia um número inteiro e
# mostre na tela se ele é par ou ímpar.

numero = int(input('Digite um número inteiro para saber se ele é par ou ímpar: '))
if numero %2 == 0:
    print(f'{numero} é um número par. ')
else:
    print(f'{numero} é um número ímpar. ')
