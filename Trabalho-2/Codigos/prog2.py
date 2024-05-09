class SistemaDeCompra:
    def __init__(self):
        self.estado_atual = 'novo acesso'
        self.produtos_disponiveis = ['Produto A', 'Produto B', 'Produto C']
        self.carrinho = []
        self.forma_pagamento = None

    def pesquisar_produtos(self, produto=None):
        if self.estado_atual == 'novo acesso':
            self.estado_atual = 'pesquisando'
            if produto:
                if produto in self.produtos_disponiveis:
                    print(f'Produto {produto} encontrado.')
                else:
                    print('Produto não encontrado.')
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

    def selecionar_produtos(self, produto):
        if self.estado_atual == 'pesquisando':
            self.carrinho.append(produto)
            return 'Produto adicionado ao carrinho.'
        else:
            return 'Ação não permitida no estado atual.'

    def visualizar_carrinho(self):
        if self.estado_atual == 'carrinho ativo':
            print('Produtos no carrinho:')
            for produto in self.carrinho:
                print(produto)
        else:
            return 'Ação não permitida no estado atual.'

    def remover_produtos(self, produto):
        if self.estado_atual == 'carrinho ativo':
            if produto in self.carrinho:
                self.carrinho.remove(produto)
                return 'Produto removido do carrinho.'
            else:
                return 'Produto não encontrado no carrinho.'
        else:
            return 'Ação não permitida no estado atual.'

    def selecionar_forma_pagamento(self, forma_pagamento):
        if self.estado_atual == 'carrinho ativo':
            self.forma_pagamento = forma_pagamento
            self.estado_atual = 'pagamento confirmado'
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

    def confirmar_dados_entrega(self, dados_entrega):
        if self.estado_atual == 'pagamento confirmado':
            print(f'Dados de entrega confirmados: {dados_entrega}')
            self.estado_atual = 'compra finalizada'
            print('Compra finalizada. Obrigado pela compra!')
            return self.estado_atual
        else:
            return 'Ação não permitida no estado atual.'

# Exemplo de uso
sistema = SistemaDeCompra()
print(sistema.pesquisar_produtos('Produto A')) # Pesquisa por um produto
print(sistema.selecionar_produtos('Produto A')) # Adiciona ao carrinho
sistema.visualizar_carrinho() # Visualiza o carrinho
print(sistema.remover_produtos('Produto A')) # Remove do carrinho
print(sistema.selecionar_forma_pagamento('Cartão de crédito')) # Seleciona forma de pagamento
print(sistema.confirmar_dados_entrega('Rua Exemplo, 123')) # Confirma dados de entrega
