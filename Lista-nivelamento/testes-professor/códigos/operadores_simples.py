class Operadores(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def somar(self):
        return self.x + self.y

    def subtrair(self):
        return self.x - self.y

    def multiplicar(self):
        return self.x * self.y

    def dividir(self):
        return self.x / self.y

if __name__ == '__main__':
    operadores = Operadores(10, 2)
    print("Soma: {:d}".format(operadores.somar()))
    print("Subtração: {:d}".format(operadores.subtrair()))
    print("Multiplicação: {:d}".format(operadores.multiplicar()))
    print("Divisão: {:d}".format(operadores.dividir()))


