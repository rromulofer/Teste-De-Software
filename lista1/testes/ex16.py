def inserir_ordenado(lista, elemento):
    index = 0
    while index < len(lista) and lista[index] < elemento:
        index += 1
    lista.insert(index, elemento)

def remover_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("O elemento não está na lista.")

def exibir_lista(lista):
    print("Lista ordenada:", lista)

def main():
    lista_ordenada = []

    while True:
        print("\nMenu:")
        print("1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Exibir lista")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            elemento = input("Digite o elemento a ser inserido: ")
            inserir_ordenado(lista_ordenada, elemento)
        elif escolha == "2":
            elemento = input("Digite o elemento a ser removido: ")
            remover_elemento(lista_ordenada, elemento)
        elif escolha == "3":
            exibir_lista(lista_ordenada)
        elif escolha == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
