# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos
# anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela
# não pode exceder 30% do salário ou o empréstimo será negado.

valor = float(input('Digite o preço da casa desejada: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite a previsão de pagamento em anos: '))
mes = (anos*12)
exceder = (salario*30/100)
prestacao = (valor/mes)
if exceder >= prestacao:
    print(f'Você vai pagar em suaves prestações de R${round(prestacao, 2)} por mês. ')
else:
    print(f'A prestação mensal R$({round(prestacao, 2)}) é maior que o valor de 30% do seu salário ', end="")
    print(f'R$({round(exceder, 2)}), portanto o empréstimo não foi aceito.')

