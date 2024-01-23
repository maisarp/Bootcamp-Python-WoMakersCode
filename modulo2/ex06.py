'''Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.'''

usuario = input('Insira o seu nome de usuário:')
senha = input('Insira a sua senha:')

while usuario != "admin" or senha != "admin123" :
    print(f'Senha incorreta.')
    usuario = input('Insira o seu nome de usuário:')
    senha = input('Insira a sua senha:')

if usuario == "admin" and senha == "admin123" :
    print(f'Acesso liberado.')