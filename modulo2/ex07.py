'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''

idade = int(input('Informe a idade do usuário (em caso de bebê considerar "0"):'))

while idade < 0 :
    print(f'Idade inválida')
    idade = int(input('Informe a sua idade:'))

if idade <= 11 :
    print(f'O usuário é uma criança.')

elif idade >= 12 and idade < 18 :
    print(f'O usuário é um adolescente.')

elif idade >= 18 and idade < 65 :
    print(f'O usuário é um adulto.')

else :
    print(f'O usuário é um idoso.')