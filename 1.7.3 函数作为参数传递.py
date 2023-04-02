def a(b):
    result = b(1, 2)
    print(result)
    return


def h(x, y):
    return x + y


a(h)
