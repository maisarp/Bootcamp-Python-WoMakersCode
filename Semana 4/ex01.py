# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

#Definição da classe 
class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 1
        self.modelo = 2
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 150
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    def acelerar(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_max:
            self.velocidade += 5
    
    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_min:
            self.velocidade -= 5

    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado} - velocidade {self.velocidade}'
    
# Crie uma instância da classe carro.
carro_1 = Carro()
carro_2 = Carro()

carro_1.ligar()
print('carro_1 está ligado? {}' .format(carro_1.ligado))
print('carro_2 está ligado? {}' .format(carro_2.ligado))
# Faça o carro "andar" utilizando os métodos da sua classe.
for _ in range(10):
    carro_1.acelerar()

print('carro_1 velocidade: {}' .format(carro_1.velocidade))
print('carro_2 velocidade: {}' .format(carro_2.velocidade))

# Faça o carro "parar" utilizando os métodos da sua classe.
'''for _ in range(10):
    carro_1.desacelerar()

print('carro_1 velocidade: {}' .format(carro_1.velocidade))
print('carro_2 velocidade: {}' .format(carro_2.velocidade))'''