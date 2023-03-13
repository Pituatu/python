# Faça um programa que peça 10 números inteiros, calcule e
# mostre a quantidade de números pares e a quantidade de números impares.
par = 0
impar = 0
for c in range(1,11):
    inteiro = int(input(f'Digite o número: '))
    if inteiro % 2 == 0:
        par = par + 1
    elif inteiro % 2 != 0:
        impar = impar + 1
print(f'são {par} números pares e {impar} números ímpares. ')
