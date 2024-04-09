from unittest import TestCase, main
from should_dsl import should
from ex3 import ConversorDeHoras

class TestConversorDeHoras(TestCase):

    def setUp(self):
        self.conversor = ConversorDeHoras()

    def test_converter_para_12_horas_horas_AM(self):
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(1, 30)
        horas_12 | should | equal_to(1)
        minutos | should | equal_to(30)
        periodo | should | equal_to("AM")

    def test_converter_para_12_horas_horas_PM(self):
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(13, 30)
        horas_12 | should | equal_to(1)
        minutos | should | equal_to(30)
        periodo | should | equal_to("PM")

    def test_converter_para_12_horas_meia_noite(self):
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(0, 0)
        horas_12 | should | equal_to(12)
        minutos | should | equal_to(0)
        periodo | should | equal_to("AM")

    def test_converter_para_12_horas_meio_dia(self):
        horas_12, minutos, periodo = self.conversor.converter_para_12_horas(12, 0)
        horas_12 | should | equal_to(12)
        minutos | should | equal_to(0)
        periodo | should | equal_to("PM")

if __name__ == "__main__":
    main()
