class Auto:
    def __init__(self,patente, modelo):
        self.patente = patente
        self.modelo = modelo
        self.estado = 1

def to_string(aut):
    print('Patente:', aut.patente, end=' ')
    print('Modelo:', aut.modelo, end=' ')
    print('Estado:', aut.estado)
    print()