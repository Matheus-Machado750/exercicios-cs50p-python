menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def pedido_completo():

    Total = 0

    while True:

        try:
            pedido = input("Item: ").title() #Converte a 1º letra em maiúscula

            if pedido in menu:

                Total = menu[pedido] + Total

                print(f"Total: ${Total:.2f}") #2 casas decimais

        except EOFError:  #Quando  o usuario termina o input (Ctrl+D)

            print() #Quebra de linha final
            break

        except KeyError:

            pass

pedido_completo()

#Obtive ajuda do ChatGPT para recordar do método .title(), adicionar o EOFError e fazer com que o output tenha 2 casas decimais
