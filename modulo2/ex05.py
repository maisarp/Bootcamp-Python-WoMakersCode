'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
'''

lado1 = float(input('Informe a medida do lado 1 do triângulo:'))
lado2 = float(input('Informe a medida do lado 2 do triângulo:'))
lado3 = float(input('Informe a medida do lado 3 do triângulo:'))

if lado1 == lado2 == lado3 :
    print(f'É um triângulo equilátero.')

elif lado1 != lado2 != lado3 :
    print(f'É um triângulo escaleno.')

else :
    print(f'É um triângulo isósceles.')