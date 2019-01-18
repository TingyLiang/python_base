from multiprocessing import Process
from multiprocessing import Pool
from queue import Queue
import os

queue = Queue()


def sub_process(name):
    print("Run sub process %s,parent is %s" % (name, os.getppid()))


if __name__ == '__main__':
    child = Process
    print("Parent process is %s" % os.getpid())
    p = Process(target=sub_process, args=("child",), name="test")
    p.start()
    p.join()
    print("End .")

    pool = Pool()
    for i in range(10):
        pool.apply_async(sub_process, args=(i,))
    print("waiting for processes done...")
    pool.close()  # join前必须先close,close 后不能再添加新的进程
    pool.join()


