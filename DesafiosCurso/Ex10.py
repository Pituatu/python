# Faça um programa que leia a largura e a altura de
# uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta o equivalente a uma área de 2m².

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = round((largura*altura),2)
litro = round((area/2),2)
print(f'A área da sua parede é {area}m², e para pintá-la serão necessários {litro}L de tinta.')

