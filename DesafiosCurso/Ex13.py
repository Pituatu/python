# Escreva um programa que converta uma temperatura digitada em ºC
# em ºF.
# Lembrando: ºF = ((9C/5) + 32)

temp = float(input("Digite uma temperatura em ºC para que ela seja convertida: "))
f = (((9*temp)/5)+32)
print(f'A temperatura {temp}ºC corresponde a {round((f), 1)}ºF. ')
