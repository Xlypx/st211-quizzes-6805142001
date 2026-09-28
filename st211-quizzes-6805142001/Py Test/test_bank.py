from bank import BankAccount


def test_deposit():
    account = BankAccount(100)
    assert account.deposit(50) == 150


def test_withdraw():
    account = BankAccount(100)
    assert account.withdraw(30) == 70


def test_invalid_deposit():
    account = BankAccount(100)

    try:
        account.deposit(-10)
        assert False
    except ValueError:
        assert True


def test_insufficient_funds():
    account = BankAccount(100)

    try:
        account.withdraw(150)
        assert False
    except ValueError:
        assert True