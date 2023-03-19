# 使用 class 當裝飾器，無參的情形
class MyDecorator:
    def __init__(self, method):
        print(method)  # 有方法使用到 @MyDecorator 就會執行
        self.method = method

    def __call__(self, *args, **kwargs):
        print("before")
        result = self.method(*args, **kwargs)
        print("after")
        return result


@MyDecorator
def m1():
    print("m1")
    return "yeah"


print(m1())
