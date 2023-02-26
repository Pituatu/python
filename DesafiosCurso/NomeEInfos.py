# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras o nome tem ao total, sem considerar espaços;
# Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo para verificar algumas informações sobre ele: '))
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))