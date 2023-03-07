# Faça um programa que leia o nome de uma pessoa e em
# seguida mostre seu primeiro e último nome.

nome = str(input('Escreva seu nome completo para que ele seja analisado: ')).strip().title()
primeiro = nome.find(' ')
ultimo = nome.rfind(' ')
print(f'Seu primeiro nome é {nome[0:primeiro]}. ')
print(f'Seu último nome é {nome[ultimo:]}. ')