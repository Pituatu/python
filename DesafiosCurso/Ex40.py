# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo.
# Abaixo de 18.5: Abaixo do peso.
# Entre 18.5 e 25: Peso normal.
# Entre 25 e 30: Sobrepreso.
# Entre 30 até 40: Obesidade.
# Acima de 40: Obesidade mórbida.
# IMC = (peso/altura²)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = (peso/(altura**2))
if imc < 18.5:
    print(f'Seu imc é {round(imc, 2)} e você está abaixo do peso. ')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu imc é {round(imc, 2)} e vocè está no seu peso ideal. ')
elif imc > 25 and imc <= 30:
    print(f'Seu imc é {round(imc, 2)} e você está com sobrepeso. ')
elif imc > 30 and imc <= 40:
    print(f'Seu imc é {round(imc, 2)} e você está com obesidade mórbida. ')
