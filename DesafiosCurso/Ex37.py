# Crie um programa que leia duas notas de um aluno e calcule sua
# média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5,0 = reprovado.
# Média entre 5,0 e 6,9 = recuperação.
# Média 7 ou superior = aprovado.

nota1 = float(input('Digite a nota da sua primeira prova: '))
nota2 = float(input('Digite a nota da sua segunda prova: '))
media = ((nota1 + nota2) / 2)
if media < 5 and media >= 0:
    print(f'Sua média foi {media} e você foi reprovado. ')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média foi {media} e você ficou de recuperação. ')
elif media >= 7 and media <= 10:
    print(f'Sua média foi {media} e você foi aprovado. ')
else:
    print('Não são notas válidas, digite novamente. ')