from threading import Thread
from queue import Queue


class MyProducer(Thread):
    def __init__(self, name: str, count: int, queue: Queue):
        super().__init__()
        self.name = name
        self.count = count
        self.queue = queue

    def run(self) -> None:
        for i in range(self.count):
            self.queue.put(f"{self.name} count={i}\n", block=True)


class MyConsumer(Thread):
    def __init__(self, name: str, queue: Queue):
        super().__init__()
        self.name = name
        self.queue = queue
        self.daemon = True  # 如果生產者都生產完了，等待也沒意義

    def run(self) -> None:
        while True:
            data = self.queue.get(block=True)
            print(f"{self.name} data={data}", end=' ')


q = Queue(5)
threads = list()
threads.append(MyProducer("p1", 8, q))
threads.append(MyProducer("p2", 8, q))
threads.append(MyProducer("p3", 8, q))

threads.append(MyConsumer("c1", q))
threads.append(MyConsumer("c2", q))

for t in threads:
    t.start()
