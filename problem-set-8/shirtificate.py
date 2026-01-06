from fpdf import FPDF


def main():
    name = input("Name: ").strip()
    create_shirtificate(name)


def create_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Fonte do título
    pdf.set_font("Helvetica", "B", 36)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)

    # Imagem da camisa
    pdf.image("shirtificate.png", x=0, y=60, w=210)

    # Texto sobre a camisa
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 24)

    pdf.set_xy(0, 110)
    pdf.cell(210, 20, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
