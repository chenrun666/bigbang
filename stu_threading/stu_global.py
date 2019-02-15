import time
import threading

count = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global count, mutex
        time.sleep(2)
        if mutex.acquire():
            count += 1
            print("I am %s, set counter:%s" % (self.name, count))
            mutex.release()


if __name__ == '__main__':
    for i in range(0, 100):
        my_thread = MyThread()
        my_thread.start()
