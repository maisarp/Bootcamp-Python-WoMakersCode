'''Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''

distancia = float (input ('Informe em quilômetros a distância percorrida: '))
combustivel = float (input ('Informe em litros a quantidade de combustível consumida: '))

#Cálculo do consumo
consumo = distancia/combustivel

print(f'O consumo médio foi {consumo}km/l')