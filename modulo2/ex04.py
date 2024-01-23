'''Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
'''
nota = -1
nota = float(input('Digite a nota de 0 a 10:'))

while nota < 0 or nota > 10 :
    print(f'Valor inválido')
    nota = float(input('Informe uma nota entre zero e dez:'))

if nota >= 7 :
    print(f'Aluno aprovado.')

else :
    print(f'Aluno reprovado.')