'''Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão'''

numero1 = int(input ('Digite o numero 01:'))
numero2 = int(input ('Digite o numero 02:'))

#Operações
soma = numero1+numero2
subtracao = numero1-numero2
divisao = numero1/numero2
multiplicacao = numero1*numero2

print(f'A soma dos números digitados é {soma}, a subtração é {subtracao}, a divisão é {divisao:.2f} e a multiplicação é {multiplicacao}.')