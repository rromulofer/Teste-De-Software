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

# Exemplo de uso
sistema = SistemaDeCompra()
print(sistema.pesquisar_produtos()) # Deve retornar 'pesquisando'
print(sistema.selecionar_produtos()) # Deve retornar 'carrinho ativo'
print(sistema.remover_produtos()) # Deve retornar 'pesquisando'
print(sistema.selecionar_forma_pagamento()) # Deve retornar 'pagamento confirmado'
print(sistema.confirmar_dados_entrega()) # Deve retornar 'compra finalizada'
