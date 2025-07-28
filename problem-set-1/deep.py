def retorna_resposta():
    pergunta = input("Qual é a resposta para a Grande Pergunta da Vida, do Universo e Tudo Mais ?").lower().strip()
    if pergunta == "42" or pergunta == "forty-two" or pergunta =="forty two":
        print ("Yes")
    else:
        print ("No")

retorna_resposta()
