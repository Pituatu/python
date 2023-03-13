# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.

contador = 0
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 < num2:
    for c in range(num1+1, num2):
        print(f'{c}', end=" " )
elif num1 > num2:
    for c in range(num1-1, num2-2, -1):
        print(f'{c}', end=" ")