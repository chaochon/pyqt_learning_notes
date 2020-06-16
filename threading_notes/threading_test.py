import threading
import time

# 定义一个全局变量  锁对象
lock = threading.Lock()

# 派生Thread类
class MyThreading(threading.Thread):
    def __init__(self, name, delay, cnt):
        super(MyThreading, self).__init__()
        self.name = name
        self.delay = delay
        self.cnt = cnt
    # 执行的函数体
    def run(self):
        print('{:s} 开始！'.format(self.name))
        print_time(self.name, self.delay, self.cnt)
        print('{:s} 结束！'.format(self.name))

def print_time(name, delay, cnt):
    time.sleep(delay)
    for _ in range(cnt):
        print('{}: {}'.format(name, time.ctime(time.time())))

def print_myname(name, cnt):

    global lock
    with lock:
        time.sleep(1)
        for n in range(cnt):
            print('{:s}: {:d}'.format(name, n+1))

if __name__=='__main__':

    # 【1】定义线程对象
    # 多线程，使用定义thread.Thread的子类
    thread_1 = MyThreading('threading_1', 1, 5)  # 定义线程对象1
    thread_2 = MyThreading('threading_2', 1, 5)

    # 多线程，使用thread.Thread函数
    thread_3 = threading.Thread(target=print_myname, args=('threading_3', 4))

    # 【2】开始启动线程
    thread_3.start()
    thread_1.start()
    thread_2.start()


    # 【3】线程对象方法join
    thread_1.join()  # 阻塞线程，直到线程1执行完毕
    thread_2.join()  # 阻塞线程，直到线程2执行完毕
    thread_3.join()

    print('退出主线程')