# Desenvolva um programa que leia o primeiro termo e
# a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

i = int(input('Digite o valor inicial da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
print(f'{i} -->', end = " ")
while c < 9:
    i = (i + r)
    c = (c + 1)
    print(f'{i} -->', end = " ")
print('Fim. ')