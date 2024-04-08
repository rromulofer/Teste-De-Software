from should import should
from ex3 import converter_para_12_horas

def test_converter_para_12_horas():
    # Testando horas AM
    horas_12, minutos, periodo = converter_para_12_horas(1, 30)
    horas_12.should.equal(1)
    minutos.should.equal(30)
    periodo.should.equal("AM")

    # Testando horas PM
    horas_12, minutos, periodo = converter_para_12_horas(13, 30)
    horas_12.should.equal(1)
    minutos.should.equal(30)
    periodo.should.equal("PM")

    # Testando meia-noite
    horas_12, minutos, periodo = converter_para_12_horas(0, 0)
    horas_12.should.equal(12)
    minutos.should.equal(0)
    periodo.should.equal("AM")

    # Testando meio-dia
    horas_12, minutos, periodo = converter_para_12_horas(12, 0)
    horas_12.should.equal(12)
    minutos.should.equal(0)
    periodo.should.equal("PM")

    # Testando horas fora do intervalo válido
    try:
        converter_para_12_horas(24, 0)
    except ValueError:
        pass
    else:
        assert False, "Horas fora do intervalo válido não lançaram exceção"

    try:
        converter_para_12_horas(-1, 0)
    except ValueError:
        pass
    else:
        assert False, "Horas fora do intervalo válido não lançaram exceção"
