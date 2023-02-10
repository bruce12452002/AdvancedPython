from threading import Thread


def my_thread(c: int):
    for i in range(c):
        print(i, end=" ")


count = (30,)
t1 = Thread(target=my_thread, name="t1", args=count)  # name沒指定，預設是 Thread-數字(從1開始)
t2 = Thread(target=my_thread, name="t2", args=count)  # daemon 為守護執行緒，主執行緒要等非守護執行緒執行完才會結束
print(t1, t2)
t1.start()
t2.start()

# 誰 join 表示，誰要執行完才能往下執行
t1.join()
t2.join()
print("finish")
