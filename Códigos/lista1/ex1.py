class Escada1:
    def __init__(self, n):
        self.n = n

    def imprimir(self):
        for i in range(1, self.n + 1):
            linha = " ".join(str(i) for _ in range(i))
            print(linha)

def main():
    n = int(input("Digite o valor de n: "))
    padrao = Escada1(n)
    padrao.imprimir()

if __name__ == "__main__":
    main()
