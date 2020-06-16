import _thread
import time


def print_time(delay, thread_name):
    time.sleep(delay)
    while 1:
        print('%s: %s' % (thread_name, time.ctime(time.time())))



if __name__=='__main__':

    try:
        # 第一个参数为执行的函数体，第二参数为参数元祖
        _thread.start_new_thread(print_time, (1,'thread_1'))
        _thread.start_new_thread(print_time, (2,'thread_2'))
    except:
        print("线程异常")

    while 1:
        pass