'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".
'''

pergunta1 = input('Telefonou para a vítima? (sim/não)')
pergunta2 = input('Esteve no local do crime? (sim/não)')
pergunta3 = input('Mora perto da vítima? (sim/não)')
pergunta4 = input('Devia para a vítima? (sim/não)')
pergunta5 = input('Já trabalhou com a vítima? (sim/não)')

lista_perguntas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]

print("Respostas:")
print(lista_perguntas)

#Contar as respostas
respostas_positivas = lista_perguntas.count("sim") #contagem da resposta "sim"

#Classificação do suspeito
if respostas_positivas == 2 :
    print(f'A pessoa é suspeita.')
elif 3 <= respostas_positivas <= 4 :
    print(f'A pessoa é cúmplice.')
elif respostas_positivas == 5 :
    print(f'A pessoa é o assassino.')
else :
    print(f'A pessoa é inocente.')