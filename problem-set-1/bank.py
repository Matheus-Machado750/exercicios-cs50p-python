def saudacao ():
    resposta = input("Qual foi a resposta do banqueiro que te atendeu ?").lower().strip()

    if resposta.startswith("hello"):
        print("$0")
    elif resposta.startswith("h"):
        print ("$20")
    else:
        print("$100")

saudacao()

#.startswith() serve pra avaliar o começo de alguma string
# Utilizei a ajuda do ChatGPT para conhecer o método .startswith()
