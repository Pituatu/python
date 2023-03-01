# Crie um programa que leia os valores do cateto oposto
# e do cateto adjacente de um triângulo retângulo e
# calcule o comprimento da hipotenusa.

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = ((co**2 + ca**2) ** (1/2))
print(f'O comprimento da hipotenusa é igual a {round((h), 2)}. ')
