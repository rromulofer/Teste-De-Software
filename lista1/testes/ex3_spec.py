from unittest import TestCase, main
from should_dsl import should, should_not
from ex3 import ConversorDeHoras

class TestConversorDeHoras(TestCase):

    def setUp(self):
        self.conversor = ConversorDeHoras()

    def test_converter_para_12_horas(self):
        # Testando horas AM
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(1, 30)
        horas_12.should.equal(1)
        minutos.should.equal(30)
        periodo.should.equal("AM")

        # Testando horas PM
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(13, 30)
        horas_12.should.equal(1)
        minutos.should.equal(30)
        periodo.should.equal("PM")

        # Testando meia-noite
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(0, 0)
        horas_12.should.equal(12)
        minutos.should.equal(0)
        periodo.should.equal("AM")

        # Testando meio-dia
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(12, 0)
        horas_12.should.equal(12)
        minutos.should.equal(0)
        periodo.should.equal("PM")

if __name__ == "__main__":
    main()
