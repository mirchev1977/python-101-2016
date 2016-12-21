def accepts(string_):
    def receiver(fun):
        def decorated(string):
            if isinstance(string, string_):
                return fun(string)
            else:
                raise ValueError('not of proper type', string_)
        return decorated
    return receiver

@accepts(str)
def say_hello(name):
    print('Hello, I am {}'.format(name))

say_hello('Kiro')
say_hello(25)
