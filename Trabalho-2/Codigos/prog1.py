class LojaOnline:
    def __init__(self):
        self.estado = Pesquisando()

    def novo_acesso(self):
        self.estado = Pesquisando()

    def pesquisar_produtos(self):
        self.estado.pesquisar_produtos()

    def selecionar_produtos(self):
        self.estado.selecionar_produtos()

    def remover_produtos(self):
        self.estado.remover_produtos()

    def selecionar_forma_pagamento(self):
        self.estado.selecionar_forma_pagamento()

    def confirmar_dados_entrega(self):
        self.estado.confirmar_dados_entrega()


class Estado:
    def pesquisar_produtos(self):
        pass

    def selecionar_produtos(self):
        pass

    def remover_produtos(self):
        pass

    def selecionar_forma_pagamento(self):
        pass

    def confirmar_dados_entrega(self):
        pass


class Pesquisando(Estado):
    def pesquisar_produtos(self):
        print("Pesquisando produtos...")
        # Lógica para pesquisar produtos
        return CarrinhoAtivo()


class CarrinhoAtivo(Estado):
    def selecionar_produtos(self):
        print("Produtos selecionados.")
        # Lógica para selecionar produtos

    def remover_produtos(self):
        print("Removendo produtos do carrinho...")
        # Lógica para remover produtos
        return Pesquisando()

    def selecionar_forma_pagamento(self):
        print("Forma de pagamento selecionada.")
        # Lógica para selecionar forma de pagamento
        return PagamentoConfirmado()


class PagamentoConfirmado(Estado):
    def confirmar_dados_entrega(self):
        print("Dados de entrega confirmados.")
        # Lógica para confirmar dados de entrega
        return CompraFinalizada()


class CompraFinalizada(Estado):
    pass
