from bill import Bill
from batch_bill import BillBatch
from cash_desk import CashDesk

# main


def main():
    # Task 1
    a = Bill(10)
    b = Bill(5)
    c = Bill(10)

    print(int(a))
    print(str(a))
    print(a)

    print(a == b)
    print(a == c)

    money_holder = {}
    money_holder[a] = 1
    print(money_holder)

    # Task 2
    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    for bill in batch:
        print(bill)

    # Task 3
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]
    batch = BillBatch(bills)

    desk = CashDesk()
    desk.take_money(batch)
    desk.take_money(Bill(10))

    desk.inspect()

if __name__ == "__main__":
    main()
