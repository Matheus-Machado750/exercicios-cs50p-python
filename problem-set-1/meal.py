def main():
    time = input("Insira o horário do dia :").strip()

    hora_convertida = convert(time)

    if 7 <= hora_convertida <= 8:
        print("breakfast time")

    elif 12 <= hora_convertida <= 13:
        print("lunch time")

    elif 18 <= hora_convertida <= 19:
        print("dinner time")


def convert(time):

    horas, minutos = time.split(":")

    horas = float(horas)
    minutos = float(minutos)

    return horas + (minutos / 60)

if __name__ == "__main__":
    main()

#Utilizei o ChatGPT pra me ajudar com a ordem dos "pedaços" das funções
