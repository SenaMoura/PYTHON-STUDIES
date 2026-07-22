class Carro:
    # O __init__ roda no momento em que o carro aparece
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.cor= cor
        self.modelo = modelo
        self.ano = ano

meu_carro = Carro("Chevrolet", "Onix", 2020, "Preto")
seu_carro = Carro("Fiat", "Argo", 2021, "Branco")

print(meu_carro.cor)
print(seu_carro.cor)