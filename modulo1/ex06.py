'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

distancia = float(input('Digite a distância de deslocamento em quilômetros: '))

# Velocidade dos veículos (km/h)
velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

#Calculo do tempo de viagem
tempo_aviao = distancia/velocidade_aviao
tempo_carro = distancia/velocidade_carro
tempo_onibus = distancia/velocidade_onibus

print(f'O tempo da viagem de avião {tempo_aviao:.2f}h, de carro é {tempo_carro:.2f}h e de ônibus {tempo_onibus:.2f}h.')