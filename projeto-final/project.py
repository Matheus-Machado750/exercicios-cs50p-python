def main():
    month = input("Insert the month for which you want to calculate expenses: ")

    all_name_list = request_expense_info()

    total_cust = calculate_total(all_name_list)

    format_table(month, all_name_list, total_cust)


def request_expense_info():
    expense_list = []

    while True:

        expense_info = input("Insert the name and cost of your expense (To stop, insert 'stop'): ").replace(" ", "")

        if expense_info.lower() == "stop":
            print("Ending...")
            break

        item = validate_expense_input(expense_info)

        if item is None:
            continue #Retorna o loop

        expense_list.append(item)

    return expense_list


def validate_expense_input(expense_info):

    parts = expense_info.split(",")

    if len(parts) != 2:
        print("Use the format: name,cost")
        return None

    expense_name, expense_cust = parts

    try:
        expense_cust = float(expense_cust)

    except ValueError:
        print("Cost must be a number.")
        return None

    if expense_cust < 0:
        print("Cost must be a positive number.")
        return None

    return (expense_name, expense_cust)


def calculate_total(lista):
    total = 0

    #Desempacotando a tupla, ignorando o primeiro valor
    for _, custo in lista:
        total += custo

    return total


def format_table(month, expenses, total):
    line = "-" * 30

    print(line)
    print(f"Expenses for: {month}")
    print(line)
    print(f"{'Expense':<15} | {'Cost':>10}")
    print(line)

    for name, cost in expenses:
        print(f"{name:<15} | {cost:>10.2f}")

    print(line)
    print(f"{'Total':<15} | {total:>10.2f}")
    print(line)


if __name__ == "__main__":
    main()
