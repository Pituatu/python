# A confederação nacional de natação precisa de um programa
# que leia a data de nascimento dos atletas e mostre sua categoria,
# de acordo com a idade.
# até 9 anos:mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 20 anos: sênior
# acima: master

from datetime import date
atual = date.today()
ano = atual.year
data = int(input('Digite seu ano de nascimento para lhe ser atribuida uma categoria: '))
idade = (ano - data)
if idade >=0 and idade <= 9:
    print(f'Você possui {idade} anos de idade e portanto faz parte da categoria mirim. ')
elif idade > 9 and idade <= 14:
    print(f'Você possui {idade} anos de idade e portanto faz parte da categoria infantil. ')
elif idade > 14 and idade <= 19:
    print(f'Você possui {idade} anos de idade e portanto faz parte da categoria junior. ')
elif idade > 19 and idade <= 20:
    print(f'Você possui {idade} anos de idade e portanto faz parte da categoria sênior. ')
elif idade > 20 and idade <= 90:
    print(f'Você possui {idade} anos de idade e portanto faz parte da categoria master. ')
elif idade > 90:
    print(f'Você não está muito velho pra estar nadando? Se ainda conseguir nadar com {idade} anos de idade , faz parte da categoria master. ')
else:
    print('Você está digitando alguma informação errada, tente de novo. ')