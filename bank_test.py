from bank import value


def main():
    test_standardcases()
    test_whitespace()
    test_cases()


def test_standardcases():
    assert value("hello") == '0'
    assert value("h") == '20'
    assert value("bonjour") == '100'


def test_whitespace():
    assert value(" hello") == '0'
    assert value("hello ") == '0'
    assert value(" hello ") == '0'


def test_cases():
    assert value("HELLO") == '0'
    assert value("hEllO") == '0'


if __name__ == "__main__":
    main()