from functools import wraps


def outer(s: str):
    # 在 decorator3.py 的基礎上，用 my_decorator 方法包起來並回傳
    def my_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"before s={s}")
            f(*args, **kwargs)
            print(f"after s={s}")

        return wrapper
    return my_decorator


@outer("a")  # 傳參
def m1():
    print("m1")


@outer("b")
def m2(s: str):
    print(f"m2 {s}")


@outer("c")
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
