print("Programa para ver costes repetidos")

for i in range(3):
    horas = float(input("Cuantas horas has trabajado? "))
    precio_hora = float(input("Cuanto vale la hora? "))

    total = horas * precio_hora

    print("El total es:", total)

    if total < 8:
        print("es barato")
    elif 8 <= total <= 15:
        print("es normal")
    else:
        print("es caro")

    print("-" * 20)  # separador visual
