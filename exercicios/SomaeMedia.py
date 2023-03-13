# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
contador = 0
for c in range(1, 6):   #contador de 1 até 5
    numero = int(input(f'Digite o {c}º valor: '))
    soma = soma + numero
    contador += 1
print(f'A soma dos números é igual a {soma} e sua média é igual a {soma/contador}. ')