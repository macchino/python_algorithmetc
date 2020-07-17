class MYException(Exception):
    pass


def devide(a, b):
    if b == 0:
        raise MYException("0では割りきれません")
    else:
        return a / b


try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))
