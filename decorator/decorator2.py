# 加上 @方法名稱，就有 decorator1.py 的功能了
def my_decorator(f):
    def wrapper(*args, **kwargs):
        print("before")
        f(*args, **kwargs)
        print("after")

    return wrapper


@my_decorator  # @ + 方法名
def m1():
    print("m1")


@my_decorator
def m2(s: str):
    print(f"m2 {s}")


@my_decorator
def m3(i: int, s: str):
    print(f"m3 {i} {s}")


m1()
print(m1, m1.__name__)
print("===============")
m2("hi")
print(m2)
print("===============")
m3(123, "hello")
print(m3)
