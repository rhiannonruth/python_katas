from palindrome_number.main import palindrome_number


def test_121():
    assert palindrome_number(121) is True


def test_minus121():
    assert palindrome_number(-121) is False


def test_10():
    assert palindrome_number(10) is False


def test_12342():
    assert palindrome_number(12342) is False


def test_minus1():
    assert palindrome_number(-1) is False