def cokeCalc():

    amont_due = 50

    while amont_due > 0:
        print(f"Amount Due: {amont_due}")

        try:
            coin = int(input("Insert Coin: "))

        except ValueError:
            continue

        if coin in (25, 10, 5):

            amont_due -= coin

    change = -amont_due if amont_due < 0 else 0

    print (f"Change Owed: {change}")


cokeCalc()

# Pedi ajuda para o ChatGPT sobre erros no check50 (erros de escrita nos "prints")
