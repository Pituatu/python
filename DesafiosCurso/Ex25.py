# Escreva um programa que faça o computador pensar em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
chute = int(input("Digite um valor de 0 até 5 para saber se você adivinhou o valor que o computador pensou: "))
x = random.randint(0,5)
if x == chute:
    print(f"Você digitou o número {chute} e o computador pensou em {x}. ")
    print(f'Parabéns, você é muito bom de adivinhação! ')
else:
    print(f'Você digitou o número {chute} e o computador pensou em {x}.')
    print(f'O computador venceu. ')