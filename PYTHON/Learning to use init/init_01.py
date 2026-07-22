# Criando uma conta bancária com o uso do método init
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        # Características de cada conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor 
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

        # O __init__ vai rodar na hora que a gente fizer a atribuição abaixo:
        conta_joao = ContaBancaria("João", 1000.0)
        conta_maria = ContaBancaria("Maria")

        conta_joao.depositar(500.0)
        #+= serve para pegar o valor que a variável já tem e somar um novo valor a ele e salva o resultado de volta na variável
        # exemplo prático: 
        #Jeito tradicional mas longo:
        #saldo = saldo + valor
        #Jeito mais curto e prático:
        #saldo += valor

        #O :. 2f serve para formatar o valor em duas casas decimais, ou seja, ele vai mostrar o valor com duas casas decimais, mesmo que seja um número inteiro. Exemplo: 1000.0 vai ser mostrado como 1000.00

        
