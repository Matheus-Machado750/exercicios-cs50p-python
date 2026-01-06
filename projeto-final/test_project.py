import project

def test_validate_expense_input_valid():
    result = project.validate_expense_input("Rent,1200")
    assert result == ("Rent", 1200.0)


def test_validate_expense_input_invalid_format():
    result = project.validate_expense_input("Rent1200")
    assert result is None


def test_validate_expense_input_invalid_cost():
    result = project.validate_expense_input("Rent,abc")
    assert result is None

def test_calculate_total():
    expenses = [
        ("Laptop", 1200.0),
        ("Food", 300.0),
        ("Internet", 100.0)
    ]

    total = project.calculate_total(expenses)
    assert total == 1600.0

def test_request_expense_info(monkeypatch):
    inputs = iter([
        "TV,1200",
        "Food,300",
        "stop"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = project.request_expense_info()

    assert result == [
        ("TV", 1200.0),
        ("Food", 300.0)
    ]
