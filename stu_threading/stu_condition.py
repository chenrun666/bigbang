"""
This class implements(执行) condition variable objects.
A condition variable allows one or more threads to wait until they are notified by another thread.
"""
import threading, time


class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)
        self.cond.acquire()
        print(f"{self.name}:我把眼睛蒙上了")
        self.cond.notify()
        self.cond.wait()

        print(f"{self.name}:我找到你了～～")
        self.cond.notify()
        self.cond.release()

        print(f"{self.name}:我赢了")


class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()

        print(f"{self.name}:我已经藏好了，来找我吧")
        self.cond.notify()
        self.cond.wait()

        self.cond.release()
        print(self.name + "被你找到了")


if __name__ == '__main__':
    cond = threading.Condition()
    seeker = Seeker(cond, "seeker")
    hider = Hider(cond, 'hider')
    seeker.start()
    hider.start()
