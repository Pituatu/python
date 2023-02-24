#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual
#de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país
#A ultrapasse ou iguale a população do país B,
#mantidas as taxas de crescimento.
a = int(80000)
b = int(200000)
x = int(0)
while a <= b:
    print(f'{a} é o valor de a.')
    print(f'{b} é o valor de b. ')
    print(f'é a população no ano de {x}.')
    x = int(x + 1)
    a = int(a +(a*(3/100)))
    b = int(b + (b*(1.5/100)))
print(f"No ano {x} a população de a se iguala ou ultrapassa a população de b. ")

