import sys
from PIL import Image, ImageOps


def main():
    check_args()

    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    # Redimensiona a imagem para caber na camisa
    image = ImageOps.fit(image, shirt.size)

    # Sobrepõe a camisa
    image.paste(shirt, shirt)

    image.save(sys.argv[2])


def check_args():
    if len(sys.argv) != 3:
        sys.exit("Invalid number of arguments")

    ext1 = sys.argv[1].lower().split(".")[-1]
    ext2 = sys.argv[2].lower().split(".")[-1]

    valid = ["jpg", "jpeg", "png"]

    if ext1 not in valid or ext2 not in valid:
        sys.exit("Invalid input")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()

