class MyIterator:
    def __init__(self, count):
        self.count = count
        self.this = 0

    def __iter__(self):
        return self

    def __next__(self):
        rtn = self.this * 2
        self.this += 1

        if self.this > self.count:
            raise StopIteration

        return rtn


for n in MyIterator(5):
    print(n)
print("===============")


def my_generator(count: int):
    for c in range(count):
        yield c * 2


for n in my_generator(5):
    print(n)
