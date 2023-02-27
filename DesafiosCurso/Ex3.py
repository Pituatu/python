# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas
# as possíveis informações sobre ele.

x = input("Digite a frase que você deseja que seja dissecada: ")
print(f'Valor primitivo da frase ou palavra digitada: {type(x)}')
print(f'Essa frase é composta somente de espaços?: {x.isspace()}')
print(f'É um número? {x.isnumeric()}. ')
print(f'É alfabético? {x.isalpha()}. ')
print(f'É alfanumérico? {x.isalnum()}.')
print(f'Está em letras maiúsculas? {x.isupper()}.')
print(f'Está em letras minúsculas? {x.islower()}.')
print(f'Está capitalizada? {x.istitle()}.')