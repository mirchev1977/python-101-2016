def get_promotion(months):
    def receiver(func):
        def decorated(user_id, number_months):
            if number_months > months:
                number_months += 1
            return func(user_id, number_months)
        return decorated
    return receiver


@get_promotion(3)
def pay_internet(user_id, number_months):
    print("user {} payed for {} months".format(user_id, number_months))


pay_internet(1, 2)
pay_internet(1, 3)
pay_internet(1, 4)
