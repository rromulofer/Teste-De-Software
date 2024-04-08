from should import should
from ex16 import inserir_ordenado, remover_elemento, exibir_lista

def test_inserir_ordenado():
    lista = [1, 3, 5]
    inserir_ordenado(lista, 4)
    lista.should.equal([1, 3, 4, 5])

def test_remover_elemento():
    lista = [1, 2, 3, 4, 5]
    remover_elemento(lista, 3)
    lista.should.equal([1, 2, 4, 5])

def test_exibir_lista():
    # A função exibir_lista imprime a lista, então você precisa capturar a saída para testar.
    # Isso pode ser feito usando o módulo 'io' para redirecionar a saída padrão para um buffer.
    import io
    import sys
    from contextlib import redirect_stdout

    lista = [1, 2, 3]
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        exibir_lista(lista)
    output = buffer.getvalue().strip()
    output.should.equal("Lista ordenada: [1, 2, 3]")
