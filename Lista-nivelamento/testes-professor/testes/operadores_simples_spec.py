from unittest import TestCase, main
from should_dsl import should
from operadores_simples import Operadores

class OperadoresTest(TestCase):

    def setUp(self):
        self.operadores = Operadores(10, 2)

    def test_somar(self):
        self.operadores.somar() | should | equal_to(12)

    def test_subtrair(self):
        self.operadores.subtrair() | should | equal_to(8)

    def test_multiplicar(self):
        self.operadores.multiplicar() | should | equal_to(20)

    def test_dividir(self):
        self.operadores.dividir() | should | equal_to(5.00)


if __name__ == '__main__':
    main()

