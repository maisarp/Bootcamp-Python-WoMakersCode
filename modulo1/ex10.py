'''Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
'''

nome = input('Informe o seu nome:')
idade = int(input('Informe sua idade:'))
trabalho = input('Sua profissão atual:')
interesse = (input('Informe a sua área de interesse:'))

print(f'Olá meu nome é {nome}, tenho {idade} anos, sou {trabalho} e tenho interesse na área de {interesse}.')