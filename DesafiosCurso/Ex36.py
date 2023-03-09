# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# O programa também deverá mostrar o tempo que falta ou
# que passou do prazo.

from datetime import date
atual = date.today()
ano = (atual.year)
data = int(input('Digite o seu ano de nascimento: '))
falta = (ano - data)
if falta < 18:
    print(f'Faltam {18 - falta} anos para você precisar se alistar. ')
elif falta == 18:
    print('Você precisa se alistar esse ano. ')
elif falta == 19:
    print(f'Você perdeu o prazo de alistamento por {falta - 18} ano.')
else:
    print(f'Você perdeu o prazo de alistamento por {falta - 18} anos.')


