# Faça um programa que leia um ano qualquer e mostre se
# ele é bissexto.

ano = int(input('Digite um ano para descobrir se ele é bissexto: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto. ')
else:
    print(f'{ano} não é um ano bissexto. ')