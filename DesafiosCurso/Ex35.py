# Escreva um programa que leia dois números inteiros e compare-os.
# Mostrando na tela uma das mensagens:
# O primeiro valor é maior.
# O segundo valor é maior.
# Os valores digitados são iguais.

num1 = int(input('Digite o primeiro valor que será comparado: '))
num2 = int(input('Digite o segundo valor da comparação: '))
if num1 > num2:
    print('O primeiro valor é maior. ')
elif num2 > num1:
    print('O segundo valor é maior. ')
else:
    print("Os valores digitados são iguais. ")