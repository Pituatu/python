# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

algo = str(input('Digite alguma coisa: '))
print(f'{type(algo)}')
print(f'{algo} só tem espaços?', algo.isspace())
print(f'{algo} é um número?' , algo.isnumeric())
print(f'{algo} é alfabético?', algo.isalpha())
print(f'{algo} é alfanumérico?.', algo.isalnum())
print(f'{algo} está em letras maiúsculas?', algo.isupper())
print(f'{algo} está em letras minúsculas?', algo.islower())
print(f'{algo} está capitalizada?', algo.istitle())