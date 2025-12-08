import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

# Caso não tenha argumentos = fonte aleatória

if len(sys.argv) == 1:
    font = random.choice(fonts)


# Caso tenha argumentos corretos

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] not in fonts:
        print("Invalid usage")
        sys.exit(1)
    font = sys.argv[2]


else:
    print("Invalid usage")
    sys.exit(1)

# Configurar fonte
figlet.setFont(font=font)

text = input("Input: ")
print("Output:")
print(figlet.renderText(text))

#tive ajuda do ChatGPT para me guiar na estrutura do código
