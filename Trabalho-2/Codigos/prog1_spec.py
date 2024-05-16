#  Prof. Antonio Eduardo Carvalho
#  Disciplina : Teste de Software
#  UENF-CCT-LCMAT-CC
#  Data: 16 de Maio de 2024
#  Aluno: Rômulo Souza Fernandes

from unittest import TestCase, main
from should_dsl import should
from prog1 import SistemaDeCompra


class TestSistemaDeCompra(TestCase):

    def setUp(self):
        self.sistema = SistemaDeCompra()

    def test_novo_acesso_pesquisar_produtos(self):
        self.sistema.estado_atual | should | equal_to('novo acesso')
        self.sistema.pesquisar_produtos() | should | equal_to('pesquisando')
        self.sistema.estado_atual | should | equal_to('pesquisando')

    def test_pesquisando_selecionar_produtos(self):
        self.sistema.estado_atual = 'pesquisando'
        self.sistema.selecionar_produtos() | should | equal_to('carrinho ativo')
        self.sistema.estado_atual | should | equal_to('carrinho ativo')

    def test_carrinho_ativo_remover_produtos(self):
        self.sistema.estado_atual = 'carrinho ativo'
        self.sistema.remover_produtos() | should | equal_to('pesquisando')
        self.sistema.estado_atual | should | equal_to('pesquisando')

    def test_carrinho_ativo_selecionar_forma_pagamento(self):
        self.sistema.estado_atual = 'carrinho ativo'
        self.sistema.selecionar_forma_pagamento() | should | equal_to('pagamento confirmado')
        self.sistema.estado_atual | should | equal_to('pagamento confirmado')

    def test_pagamento_confirmado_confirmar_dados_entrega(self):
        self.sistema.estado_atual = 'pagamento confirmado'
        self.sistema.confirmar_dados_entrega() | should | equal_to('compra finalizada')
        self.sistema.estado_atual | should | equal_to('compra finalizada')

    def test_acao_nao_permitida(self):
        self.sistema.estado_atual = 'carrinho ativo'

        resultado = self.sistema.pesquisar_produtos()

        resultado | should | equal_to('Ação não permitida no estado atual.')

if __name__ == "__main__":
    main()
