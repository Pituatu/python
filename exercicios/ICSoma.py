# Faça um programa que receba dois números inteiros e gere os números
# inteiros que estão no intervalo compreendido por eles.
# faça a soma dos números do intervalo.

soma = 0
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 < num2:
    for c in range(num1+1, num2):
        soma = soma + c
        print(f'{c}', end=" " )
    print(f'\nA soma dos valores resulta em {soma}. ')
elif num1 > num2:
    for c in range(num1-1, num2-2, -1):
        soma = soma + c
        print(f'{c}', end=" ")
    print(f'\nA soma dos valores resulta em {soma}. ')