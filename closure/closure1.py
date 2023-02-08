def my_closure():
    a = 1

    def inner():
        print(a)

    a = 2
    return inner


my_closure()()

# __closure__
fn = my_closure()

# 下一行 debug 看 evaluate expression 內容，會發現 a 的值會被複製到 inner 裡，原本的 a 在方法執行完就結束了
print(fn.__closure__)
