def extensao ():
    pergunta = input("Qual é o nome do aquivo ?").strip().lower()


    if pergunta.endswith(".gif"):
        print("image/gif")

    elif pergunta.endswith((".jpg", ".jpeg")):
        print("image/jpeg")

    elif pergunta.endswith(".png"):
        print("image/png")

    elif pergunta.endswith(".pdf"):
        print("application/pdf")

    elif pergunta.endswith(".txt"):
        print("text/plain")

    elif pergunta.endswith(".zip"):
        print("application/zip")

    else:
        print("application/octet-stream")

extensao()

#Realizei uma pesquisa no Google prra conhecer o método ".endswith" e pedi ajuda do ChatGpt para saber como colocar 2 argumentos dento de uma mesmo método
