class SistemaDeCompra:
    def __init__(self):
        self.estado_atual = 'novo acesso'

    def pesquisar_produtos(self):
        if self.estado_atual == 'novo acesso':
            self.estado_atual = 'pesquisando'
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

    def selecionar_produtos(self):
        if self.estado_atual == 'pesquisando':
            self.estado_atual = 'carrinho ativo'
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

    def remover_produtos(self):
        if self.estado_atual == 'carrinho ativo':
            self.estado_atual = 'pesquisando'
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

    def selecionar_forma_pagamento(self):
        self.estado_atual = 'carrinho ativo'
        if self.estado_atual == 'carrinho ativo':
            self.estado_atual = 'pagamento confirmado'
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

    def confirmar_dados_entrega(self):
        if self.estado_atual == 'pagamento confirmado':
            self.estado_atual = 'compra finalizada'
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

sistema = SistemaDeCompra()
print(sistema.pesquisar_produtos())
print(sistema.selecionar_produtos())
print(sistema.remover_produtos())
print(sistema.selecionar_forma_pagamento())
print(sistema.confirmar_dados_entrega())
