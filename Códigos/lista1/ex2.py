class Escada2:

    def __init__(self, n):
        self.n = n

    def imprimir(self):
        for i in range(1, self.n + 1):
            linha = " ".join(str(j) for j in range(1, i + 1))
            print(linha)

def main():
    n = int(input("Digite o valor de n: "))
    padrao = Escada2(n)
    padrao.imprimir()

if __name__ == "__main__":
    main()
