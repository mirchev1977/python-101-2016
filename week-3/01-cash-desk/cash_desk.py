from bill import Bill, CountedBill
from batch_bill import BillBatch


class CashDesk:
    def __init__(self):
        self.total = 0
        self.banknotes = {}

    def take_money(self, inp):
        if isinstance(inp, BillBatch):
            for x in inp:
                self.total += x.amount
                self.collect_banknotes(x)
        elif isinstance(inp, Bill):
            self.total += inp.amount
            self.collect_banknotes(inp)

    def sort_banknotes(self):
        lst = []
        for x in self.banknotes:
            banknote = int(str(x).split('$')[0].split(' ')[1])
            number_of_type = self.banknotes[x]
            banknote_key = x
            counted_bill = CountedBill(banknote, number_of_type, banknote_key)
            lst.append(counted_bill)

        lst.sort(key=lambda x: x.amount)
        return lst

    def inspect(self):
        print("We have a total of {}$ in the desk".format(self.total))
        print('# We have the following count of bills, sorted in ascending order:')
        sorted_banknotes = self.sort_banknotes()

        for banknote in sorted_banknotes:
            print("{}$ bills - {}".format(banknote.amount, banknote.bill_count))

    def collect_banknotes(self, inp):
        if inp in self.banknotes:
            self.banknotes[inp] += 1
        else:
            self.banknotes[inp] = 1
