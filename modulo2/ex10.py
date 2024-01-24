''' Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

numero1 = int(input('Insira o primeiro número:'))
numero2 = int(input('Insira o segundo número:'))
numero3 = int(input('Insira o terceiro número:'))

lista_numeros = []
lista_numeros.append(numero1)
lista_numeros.append(numero2)
lista_numeros.append(numero3)

lista_numeros.sort() #ordenando a lista em ordem crescente

print(lista_numeros)