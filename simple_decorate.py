
def deco(func):
    print("i am a decorater!!")
    return func


@deco
def add(x, y):
    return x + y


# 等价于add = deco(add)
# deco()的返回值必须可调用


if __name__ == '__main__':
    add(2, 3)
