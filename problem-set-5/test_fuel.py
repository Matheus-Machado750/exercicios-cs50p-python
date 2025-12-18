from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_convert_invalid():
    try:
        convert("cat/dog")
        assert False
    except ValueError:
        pass


def test_convert_negative():
    try:
        convert("-1/2")
        assert False
    except ValueError:
        pass


def test_convert_zero_division():
    try:
        convert("1/0")
        assert False
    except ZeroDivisionError:
        pass


def test_gauge_empty():
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"


def test_gauge_percentage():
    assert gauge(50) == "50%"