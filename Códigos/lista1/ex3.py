def converter_para_12_horas(horas, minutos):
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


def main():
    while True:
        try:
            horas = int(input("Digite as horas (0-23): "))
            minutos = int(input("Digite os minutos (0-59): "))

            if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                print("Entrada inválida! Por favor, insira valores válidos.")
                continue

            horas_12, minutos, periodo = converter_para_12_horas(horas, minutos)
            print(f"A hora convertida é: {horas_12}:{minutos:02d} {periodo}")

            continuar = input("Deseja converter outra hora? (s/n): ").strip().lower()
            if continuar != 's':
                break
        except ValueError:
            print("Por favor, insira valores inteiros válidos para horas e minutos.")


if __name__ == "__main__":
    main()
