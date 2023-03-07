# Crie um programa que leia o nome de uma pessoa e diga se ela
# tem "SILVA" no nome.

nome = str(input('Digite o seu nome para que ele seja analisado: ')).upper().strip()
divisa = nome.split()
print(f'SILVA' in divisa)




