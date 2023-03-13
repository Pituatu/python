# Crie um programa que faça o computador jogar jokenpô
# com você.

import random
jokenpo = str(input('Digite pedra, papel ou tesoura para jogar contra o computador: ')).lower()
x = random.randint(1, 3)
if jokenpo == 'pedra':
    if x == 1:
        print('O computador jogou pedra também, portanto é um \033[32mempate\033[m. ')
    if x == 2:
        print('O computador jogou papel, portanto você \033[31mperdeu\033[m. ')
    if x == 3:
        print('O computador jogou tesoura, portanto você \033[36mganhou\033[m. ')
elif jokenpo == 'papel':
    if x == 1:
        print('O computador jogou pedra, portanto você \033[34mganhou\033[m. ')
    if x == 2:
        print('O computador jogou papel também, e portanto é um \033[32mempate\033[m. ')
    if x == 3:
        print('O computador jogou tesoura, e portanto você \033[31mperdeu\033[m. ')
elif jokenpo == 'tesoura':
    if x == 1:
        print('O computador jogou pedra e portanto você \033[31mperdeu\033[m. ')
    if x == 2:
        print('O computador jogou papel, e portanto você \033[34mganhou\033[m. ')
    if x == 3:
        print('O computador jogou tesoura também, e portanto é um \033[32mempate\033[m. ')
else:
    print('Você só deve digitar pedra, papel ou tesoura para jogar. ')

