# Elabore um programa que calcule o valor a ser pago por um produto.
# Considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque : 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal.
# Em 3x ou mais no cartão: 20% de juros.
import math
preco = float(input('Digite o preço do produto que você vai comprar: '))
print('Para pagar à vista com dinheiro/cheque, digite 1: ')
print('Para pagar à vista no cartão, digite 2: ')
print('Para pagar em até 2x no cartão, digite 3: ')
print('Para pagar em 3x ou mais no cartão. digite 4: ')
dinheiro = (preco - (preco * 10/100))
card1 = (preco - (preco * 5/100))
card2 = (preco + (preco * 20/100))
condicao = str(input('Digite a forma de pagamento: '))
if condicao == '1':
    print(f'Você recebeu 10% de desconto no produto que vale R${preco} e portanto precisa pagar R${dinheiro}. ')
elif condicao == '2':
    print(f'Você recebeu 5% de desconto no produto que vale R${preco} e portanto precisa pagar R${card1}. ')
elif condicao == '3':
    print(f'Você vai pagar o valor normal de R${preco}. ')
elif condicao == '4':
    print(f'Você recebeu juros de 20% no produto que vale R${preco} e portanto precisa pagar R${card2}. ')
else:
    print('Digite uma forma de pagamento válida. ')