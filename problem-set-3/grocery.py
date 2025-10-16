def lista_compras():

    lista = {}

    while True:

        try:

            itens = input("").strip().upper()

            if itens in lista: #Se tal input já existir, soma 1
                lista[itens] += 1

            else:
                lista[itens] = 1 #Se não existir, começa a contar

        except EOFError:

            break

        except KeyError:

            pass

    for itens in sorted(lista.keys()): #Percorre os itens em ordem alfabétia

        print(lista[itens], itens)

lista_compras()