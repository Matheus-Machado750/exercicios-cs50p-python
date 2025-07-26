def convert (text_emoji):
    text_emoji = text_emoji.replace(":)", "🙂")
    text_emoji = text_emoji.replace(":(", "🙁")

    return text_emoji

def main ():
    text = input("Diga uma mensagem :")
    text = convert(text)
    print (text)

main()

