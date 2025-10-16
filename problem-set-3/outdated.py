meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def formata_data():
    while True:
        try:
            data = input("Date: ").strip()

            if "/" in data:
                mes, dia, ano = data.split("/")

            elif "," in data:
                parte_mes, parte_ano = data.split(",")
                mes_nome, dia = parte_mes.strip().split(" ")
                mes = str(meses.index(mes_nome) + 1)
                ano = parte_ano.strip()

            else: # Se não tiver nem "/" nem ","
                continue

            mes = int(mes)
            dia = int(dia)
            ano = int(ano)

            if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                continue

            # Saída formatada: YYYY-MM-DD
            print(f"{ano:04}-{mes:02}-{dia:02}")
            break

        except (ValueError, IndexError):
            continue

formata_data()