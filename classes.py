class Circulo: 
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor

circulo_primeiro = Circulo()
print(id(circulo_primeiro), circulo_primeiro.cor)
circulo_primeiro.troca_cor('Vermelho')
print(id(circulo_primeiro), circulo_primeiro.cor)
