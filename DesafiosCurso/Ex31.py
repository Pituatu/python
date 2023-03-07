# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# para salário superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: '))
superior = (salario + (salario*10/100))
inferior = (salario + (salario*15/100))
if salario > 1250:
    print(f'Você receberá um aumento de 10% no seu antigo salário. ')
    print(f'O seu antigo salário era R${salario}, com o reajuste ele se tornou R${round(superior, 3)}. ')
else:
    print(f'Você receberá um aumento de 15% no seu antigo salário. ')
    print(f'O seu antigo salário era R${salario}, com o reajuste ele se tornou R${round(inferior, 3)}. ')