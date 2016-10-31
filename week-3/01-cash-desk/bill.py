class Bill:
    def __init__(self, amount):
        self.validate_integer(amount)
        self.amount = self.validate_amount(amount)

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, bill):
        if(bill.amount == self.amount):
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__str__())

    def validate_amount(self, amount):
        if amount < 0:
            raise ValueError("cant't enter negative amount of money")

        return amount

    def validate_integer(self, amount):
        if not isinstance(amount, int):
            raise TypeError(
                "the amount you enter should be integer(whole number)")

        return amount


class CountedBill(Bill):
    """docstring for ClassName"""
    def __init__(self, amount, bill_count, banknote_key):
        super().__init__(amount)
        self.bill_count = bill_count
        self.banknote_key = banknote_key
        