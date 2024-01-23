'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = str(input('Digite o turno que você estuda. Use M-matutino ou V-Vespertino ou N- Noturno.'))

if turno == 'M' :
    print(f'Bom Dia!')

elif turno == 'V' :
    print(f'Boa Tarde!')

elif turno == 'N' :
    print(f'Boa Noite!')

else :
    print(f'Valor Inválido!')