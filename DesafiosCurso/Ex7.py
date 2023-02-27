# Escreva um programa que peça um valor em metros e
# o exiba convertido em centímetros e milimetros.

n1 = float(input("Digite o valor em metros que deseja converter: "))
n2 = (n1*1000)
n3 = (n1*100)
n4 = (n1*10)
n5 = (n1/10)
n6 = (n1/100)
n7 = (n1/1000)
print(f'{n1}m é igual a {n2}mm. ')
print(f'{n1}m é igual a {n3}cm. ')
print(f'{n1}m é igual a {n4}dm. ')
print(f'{n1}m é igual a {n5}dam. ')
print(f'{n1}m é igual a {n6}hm. ')
print(f'{n1}m é igual a {n7}km.')
