import operator


class Calculadora(object):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def somar(self) -> float:
        return operator.add(self.__x, self.__y)

    def subtrair(self) -> float:
        return operator.sub(self.__x, self.__y)

    def multiplicar(self) -> float:
        return operator.mul(self.__x, self.__y)

    def dividir(self) -> float:
        return operator.truediv(self.__x, self.__y)


if __name__ == '__main__':
    calculadora = Calculadora(10, 3)
    print("Soma: {:.2f}".format(calculadora.somar()))
    print("Subtração: {:.2f}".format(calculadora.subtrair()))
    print("Multiplicação: {:.2f}".format(calculadora.multiplicar()))
    print("Divisão: {:.2f}".format(calculadora.dividir()))