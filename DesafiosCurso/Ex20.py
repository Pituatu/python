# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras o nome possui ao total, sem contar os espaços;
# Quantas letras o primeiro nome tem.

nome = (input('Digite o seu nome para que ele seja analisado: '))
print(nome.upper())
print(nome.lower())
tamanho = (len(nome) - (nome.count(" ")))
print(f'Seu nome possui {tamanho} letras. ')
divide = nome.split()
print(f'Seu primeiro nome é {divide[0]} e ele possui {len(divide[0])} letras. ')