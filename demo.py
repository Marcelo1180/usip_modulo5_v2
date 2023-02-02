class Automovil:
    def __init__(self, nombre):
        self.__placa = nombre

    def mostrarme_placa(self):
        return self.__placa

minibus = Automovil("XYZ-123")
print(minibus.mostrarme_placa())
