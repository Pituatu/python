#Supondo que a população de um país A seja da ordem de p1 habitantes com uma taxa anual
#de crescimento de t1 e que a população de B seja p2 habitantes com uma taxa de crescimento de t2.
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país
#A ultrapasse ou iguale a população do país B,
#mantidas as taxas de crescimento.
p1 = int(input("Digite a população do país A: "))
t1 = float(input("Digite a taxa de crescimento da populaçao do país A. O valor será convertido em porcentagem: "))
p2 = int(input('Digite a população do país B: '))
t2 = float(input("Digite a taxa de crescimento da população do país B. O valor será convertido em porcentagem: "))
x = int(0)
while p1 <= p2:
    print(f'{p1} é o valor de a.')
    print(f'{p2} é o valor de b. ')
    print(f'é a população no ano de {x}.')
    x = int(x + 1)
    p1 = int(p1 +(p1*(t1/100)))
    p2 = int(p2 + (p2*(t2/100)))
print(f"No ano {x} a população de a se iguala ou ultrapassa a população de b. ")