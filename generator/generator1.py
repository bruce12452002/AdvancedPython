def my_generator():
    print("a")
    yield 111
    print("b")
    yield 222
    print("c")
    yield 333


print(my_generator())
print("===============")

my = my_generator()
# print(next(my))
# print(next(my))
# print(next(my))
# next(my)  # 超過會報錯

print("===============")
# 如果已執行過就不會再執行
for m in my:
    print(m)
