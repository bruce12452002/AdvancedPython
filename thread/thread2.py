import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name: str, count: int):
        super().__init__()
        # self.setName(name)  # 3.10 版被標記為棄用，改用下一行的方式
        self.name = name
        self.count = count

    def run(self) -> None:
        for i in range(self.count):
            # print(f"{self.getName()}", end=" ")   # 3.10 版被標記為棄用，改用下一行的方式
            # print(f"{self.name} count={i}")
            print(f"{self.name} count={i}\n", end="")  # 印的時候，換行和要顯示的字一組的，不分開
            time.sleep(1 / 100)


c = 50
t1 = MyThread("t1", c)
t2 = MyThread("t2", c)
t1.start()
t2.start()
