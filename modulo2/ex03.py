'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.'''

nota = -1 #declarando a váriavel e atribuindo o valor
nota = int(input('Informe uma nota entre zero e dez:'))

while nota < 0 or nota > 10 :
    print(f'Valor inválido')
    nota = float(input('Informe uma nota entre zero e dez:'))
          
print(f'Valor válido, obrigada!')