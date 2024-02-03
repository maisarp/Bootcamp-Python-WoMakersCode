'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''

#Inicializando contadores
par = 0
impar = 0 

while True : #execução do loop infinito
    numero = int(input('Insira um número positivo (digite 0 para encerrar o programa):'))

    if numero == 0:
        break

    if numero > 0 :
        if numero % 2 == 0 :
            par += 1 #incrementa 1 aos numeros pares
        else :
            impar += 1

    else :
        print(f'Por favor, insira um número positivo:')

print(f'Quantidade de números pares: {par}')
print(f'Quantidade de números ímpares: {impar}')