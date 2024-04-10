class ListaOrdenada:
    def __init__(self):
        self.lista_ordenada = []

    def inserir_ordenado(self, elemento):
        index = 0
        while index < len(self.lista_ordenada) and self.lista_ordenada[index] < elemento:
            index += 1
        self.lista_ordenada.insert(index, elemento)

    def remover_elemento(self, elemento):
        if elemento in self.lista_ordenada:
            self.lista_ordenada.remove(elemento)
        else:
            print("O elemento não está na lista.")

    def exibir_lista(self):
        print("Lista ordenada:", self.lista_ordenada)


def main():
    lista_ordenada = ListaOrdenada()
    while True:
        print("\nMenu:")
        print("1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Exibir lista")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            elemento = input("Digite o elemento a ser inserido: ")
            lista_ordenada.inserir_ordenado(elemento)
        elif escolha == "2":
            elemento = input("Digite o elemento a ser removido: ")
            lista_ordenada.remover_elemento(elemento)
        elif escolha == "3":
            lista_ordenada.exibir_lista()
        elif escolha == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
