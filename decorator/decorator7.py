# 使用方法當裝飾器接收類別
def my_decorator(cls):
    print("yeah1")
    c = cls
    print("yeah2")
    return c


def my_decorator2(cls):
    print("yeah")

    def inner():
        print("before")
        o = cls()
        print("after")
        return o
    return inner


@my_decorator
# @my_decorator2
class Animal:
    pass


Animal()

# 使用 @my_decorator，只會印一次 yeah1 和 yeah2，因為類別初始化只有一次
# 使用 @my_decorator，仍然只會印一次 yeah1 和 yeah2，但回傳的方法每次都會調用
Animal()
