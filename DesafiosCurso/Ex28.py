# Desenvolva um programa que pergunte a distância de
# uma viagem em Km. Calcule o preço da passagem, cobrando
# R$0,50 por Km para viagens de até 200Km e R$0,45 para
# viagens mais longas.

distancia = float(input("Digite a distância do destino pretendido em Km: "))
menor = (distancia*0.50)
maior = (distancia*0.45)
if distancia <= 200:
    print('Por ser uma viagem de até 200Km, você vai pagar R$0,50 por Km.')
    print(f'Você vai pagar R${menor} na passagem.')
else:
    print('Por ser uma viagem maior que 200Km, você vai pagar R$0,45 por Km.')
    print(f'Você vai pagar R${maior} na passagem. ')
