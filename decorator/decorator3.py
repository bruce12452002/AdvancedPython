from functools import wraps


def my_decorator(f):
    # 印出 m1 方法名時，本來會有 wrapper 的資訊，用了這個裝飾器就只會印出 m1 本身，也就是看起來和沒使用裝飾器一樣
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("before")
        f(*args, **kwargs)
        print("after")

    return wrapper


@my_decorator
def m1():
    print("m1")


@my_decorator
def m2(s: str):
    print(f"m2 {s}")


@my_decorator
def m3(i: int, s: str):
    print(f"m3 {i} {s}")


m1()
print(m1)
print("===============")
m2("hi")
print(m2)
print("===============")
m3(123, "hello")
print(m3)
print(m3.__name__)
