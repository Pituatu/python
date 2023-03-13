# Faça um programa que leia 5 números e informe o maior número.

maior = 0
for c in range(1, 6):   #contador de 1 até 5
    numero = int(input(f'Digite o {c}º valor: '))
    if numero > maior:
        maior = numero
print(maior)

