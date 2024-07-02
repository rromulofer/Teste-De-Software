class ConversorDeHoras:
    def __init__(self):
        pass

    def converter_para_12_horas(self, horas, minutos):
        if horas > 12:
            horas_12 = horas - 12
            periodo = "PM"
        elif horas == 0:
            horas_12 = 12
            periodo = "AM"
        elif horas == 12:
            horas_12 = 12
            periodo = "PM"
        else:
            horas_12 = horas
            periodo = "AM"

        return horas_12, minutos, periodo

    def main(self):
        while True:
            try:
                horas = int(input("Digite as horas (0-23): "))
                minutos = int(input("Digite os minutos (0-59): "))

                if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                    print("Entrada inválida, insira valores válidos.")
                    continue

                horas_12, minutos, periodo = self.converter_para_12_horas(horas, minutos)
                print(f"A hora convertida é: {horas_12}:{minutos:02d} {periodo}")

                continuar = input("Deseja converter novamente? (s/n): ").strip().lower()
                if continuar != 's':
                    break
            except ValueError:
                print("Insira valores inteiros válidos para horas e minutos.")


if __name__ == "__main__":
    conversor = ConversorDeHoras()
    conversor.main()
