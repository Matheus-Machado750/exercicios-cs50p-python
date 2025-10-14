def main():

    fuel = ask_fraction()
    if fuel <= 1:
        print ("E")

    elif fuel >= 99:
        print ("F")

    else:
        print (f"{fuel}%")


def ask_fraction():

    while True: #Só para quando o input estiver de aacordo com o solicitado

        try:
            fraction = input("Insert a fraction: ") #Pede uma fração pro user
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x < 0 or y < 0: #Evita passar números negativos

                continue

            if y == 0: #Evita a divisão por 0

                continue #Se ocorrer isso, o continue faz voltar o código no começo do While

            if x > y: #Nenhuma divisão maior que 1

                continue


            porcentagem = round((x / y) * 100) #Cálculo da porcentagem

            return porcentagem


        except(ValueError, ZeroDivisionError):
        #ValueError caso não consiga converter pra inteiro
        #ZeroDivisonError caso ainda passe

            pass

(main())
