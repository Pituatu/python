# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input("Digite seu usuário: "))
senha = str(input("Digite a sua senha: "))
while usuario == senha:
    print("Por favor, digite uma senha e um usuário diferente. ")
    usuario = str(input("Digite seu usuário: "))
    senha = str(input("Digite a sua senha: "))
else:
    print("Usuário e senha confirmados. ")
