def main():
    expressao = input("Expression: ").strip()
    x_str, y, z_str = expressao.split()

    x = float(x_str)
    z = float(z_str)

    if y == "+":
        return x + z

    elif y == "-":
        return x - z

    elif y == "*":
        return x * z

    elif y == "/":
        return x / z

    else:
        return None


def calculo():
    resultado = main()

    if resultado is None:
        return

    print(f"{resultado:.1f}")

calculo()

#Utilizei o ChatGpt para a correção de erros e ajuda para aprender sobre o "split"
