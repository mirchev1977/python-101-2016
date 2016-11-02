from bank_account import BankAccount


def main():
    bank_account = BankAccount("Kirkor Kirkorov", 100, "dollars")
    bank_account.deposit(500)
    print(bank_account.balance())
    bank_account.withdraw(200)
    print(bank_account.balance())
    print(bank_account)
    print(int(bank_account))

    account_1 = BankAccount("Panajot", 500, "euros")
    account_2 = BankAccount("Panajot", 500, "dollars")

    print(bank_account == account_1)
    print(bank_account == account_2)

    print(bank_account.transfer_to(account_1, 100))
    print(bank_account.transfer_to(account_2, 100))

    print(bank_account)
    print(account_1)
    print(account_2)

    print(bank_account.history())
    # account = BankAccount("Rado", 0, "$")
    # print(account)
    # account.deposit(1000)
    # account.balance()
    # str(account)
    # int(account)
    # account.history()
    # account.withdraw(500)
    # account.balance()
    # account.history()
    # account.withdraw(1000)
    # account.balance()
    # print(account.history())


if __name__ == "__main__":
    main()
