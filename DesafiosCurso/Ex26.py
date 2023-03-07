# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar os 80km/h, mostre uma mensagem
# dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada Km acima do limite.

velocidade = int(input("Digite a velocidade que vocè estava quando passou pelo radar: "))
acima = ((velocidade - 80)*7)
if velocidade > 80:
    print(f'Você foi multado por ultrapassar o limite de 80Km/h.')
    print(f'O valor da multa é de R$7,00 por km acima do limite, totalizando R${float(round(acima, 2))} no total. ')
else:
    print('Felizmente você estava abaixo de 80Km/h quando passou pelo radar e não foi multado. ')