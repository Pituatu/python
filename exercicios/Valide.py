# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input('Digite seu nome: '))
while len(nome) <= 3:
    nome = str(input('Digite seu nome novamente, com mais de 3 caracteres: '))

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Digite uma idade válida entre 0 e 150: '))

salario = float(input('Digite o seu salário: '))
while salario < 0:
    salario = float(input('Digite um salário maior que 0: '))

sexo = str(input('Digite o seu sexo [f] ou [m]: ')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo: ')).upper()

estado = str(input('Digite seu estado civil: solteiro[s], casado[c], viúvo(a)[v] ou divorciado[d]: '))
while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
    estado = str(input('Digite seu estado civil: solteiro[s], casado[c], viúvo(a)[v] ou divorciado[d]: '))
else:
    print("Suas informações foram salvas. ")





