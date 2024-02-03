'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.'''

km = int (input('Informe a quantidade de quilômetros: '))

#Cálculo da distância
metros = km*1000
cm = metros*100
mm = cm*10

print(f'{km} km correspondem a {metros} metros, {cm} centímetros e {mm} milímetros.')