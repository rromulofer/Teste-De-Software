from unittest import TestCase, main
from should_dsl import should
from io import StringIO
from contextlib import redirect_stdout
from ex16 import ListaOrdenada

class TestListaOrdenada(TestCase):

    def test_inserir_ordenado(self):
        lista = ListaOrdenada()
        lista.inserir_ordenado(4)
        lista.lista_ordenada | should | equal_to([4])

    def test_remover_elemento(self):
        lista = ListaOrdenada()
        lista.lista_ordenada = [1, 2, 3, 4, 5]
        lista.remover_elemento(3)
        lista.lista_ordenada | should | equal_to([1, 2, 4, 5])

    def test_exibir_lista(self):
        lista = ListaOrdenada()
        lista.lista_ordenada = [1, 2, 3]
        buffer = StringIO()
        with redirect_stdout(buffer):
            lista.exibir_lista()
        output = buffer.getvalue().strip()
        output | should | equal_to("Lista ordenada: [1, 2, 3]")

if __name__ == "__main__":
    main()
