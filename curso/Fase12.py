nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Renato' or nome == 'Regina':
    print('Seu nome é legalzinho. ')
elif nome in 'Maria Carlos João José' :
    print('Você tem nome de velho.')
else:
    print('Seu nome não é tão legal. ')
print(f'Tenha um bom dia, {nome}. ')