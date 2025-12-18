from plates import is_valid

def test_length():

    assert is_valid("Math") == (True)
    assert is_valid("M") == (False)
    assert is_valid("Matheus") == (False)

def test_start_two_letters():

    assert is_valid("MA75") == (True)
    assert is_valid("M700") == (False)
    assert is_valid("072M") == (False)

def test_middle_numbers():

    assert is_valid("MT555") == (True)
    assert is_valid("MA75A") == (False)
    assert is_valid("THE83A") == (False)

def test_0_first_number():

    assert is_valid("EM745") == (True)
    assert is_valid("M078") == (False)
    assert is_valid("WM007") == (False)

def test_punctuation():

    assert is_valid("MAKD") == (True)
    assert is_valid("PAJ_40") == (False)
    assert is_valid("KF--H") == (False)