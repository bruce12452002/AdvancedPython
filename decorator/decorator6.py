# 使用 class 當裝飾器，有參的情形
class MyDecorator:
    def __init__(self, num):
        self.num = num

    def __call__(self, method):
        def wrapper(*args, **kwargs):
            print(f"before {self.num}")
            result = method(*args, **kwargs)
            print("after")
            return result

        return wrapper


@MyDecorator(100)
def m2():
    print("m2")
    return "yeah"


print(m2())
