from bank import value

def test_hello():
    assert value("hello, Matheus") == 0
    assert value("Hello, Matheus") == 0
    assert value("HELLO, Matheus") == 0

def test_h():
    assert value("hi, Matheus") == 20
    assert value("Hi, Matheus") == 20
    assert value("HI, Matheus") == 20


def test_random_word():
    assert value("pizza") == 100
    assert value("good morning") == 100

def test_numbers():
    assert value("075") == 100