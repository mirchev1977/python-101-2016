class BankAccount:
    """docstring for BankAccount"""

    def __init__(self, name, balance, currency):
        self.currencies = {"dollars": "$", "euros": "EUR", "levs": "BGN"}
        self.__name = name
        self.__balance = self.__validate_positive_value(balance)
        self.__currency = currency
        self.__history = []
        self.__history.append('Account was created')

    def __validate_positive_value(self, balance):
        if balance < 0:
            raise ValueError('the sum should be positive number or 0')
        return balance

    def deposit(self, amount):
        amount = self.__validate_positive_value(amount)
        self.__history.append('deposited {} {}'.
                              format
                              (amount, self.currencies[self.__currency]))
        self.__balance += amount

    def balance(self):
        self.__history.append('Balance check -> {}{}'.
                              format(self.__balance, self.currencies[self.__currency]))
        return self.__balance

    def withdraw(self, amount):
        amount = self.__validate_positive_value(amount)
        if self.__balance > amount:
            self.__balance -= amount
            self.__history.append('{}{} was withdrawed'.
                                  format(amount, self.currencies[self.__currency]))
            return True
        else:
            self.__history.append('Withdraw for {}{} failed.'.
                                  format(amount, self.currencies[self.__currency]))
            return False

    def __str__(self):
        return "Bank account for {} with balance of {} {}".\
            format(self.__name, self.__balance,
                   self.currencies[self.__currency])

    def __int__(self):
        self.__history.append('__int__ check -> {}{}'.
                              format(self.__balance, self.currencies[self.__currency]))
        return self.__balance

    def __eq__(self, account):
        if self.__currency == account.__currency:
            return True
        else:
            return False

    def transfer_to(self, account, amount):
        amount = self.__validate_positive_value(amount)
        if self.__eq__(account):
            self.withdraw(amount)
            account.deposit(amount)
            self.__history.\
                append('Transfer to {} for {}{}'.
                       format(account.__name, amount, self.currencies[self.__currency]))
            return True
        else:
            self.__history.append('Transfer for {}{} to {} failed.'.
                                  format
                                  (amount, self.currencies[self.__currency], account.__name))
            return False

    def history(self):
        return self.__history
