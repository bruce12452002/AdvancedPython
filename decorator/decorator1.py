# m1 m2 m3 這三個方法，都想在開始和結束做一樣的事

def my_decorator(f):
    def wrapper(*args, **kwargs):
        print("before")
        f(*args, **kwargs)
        print("after")

    return wrapper


def m1():
    print("m1")


def m2(s: str):
    print(f"m2 {s}")


def m3(i: int, s: str):
    print(f"m3 {i} {s}")


my_decorator(m1)()
print(m1, my_decorator(m1))
print("===============")
my_decorator(m2)("hi")
print(m2, my_decorator(m2))
print("===============")
my_decorator(m3)(123, "hello")
print(m3, my_decorator(m3))
