import queue
from multiprocessing.managers import BaseManager
from queue import Queue

task_que = Queue()
result_que = Queue()


### 分布式进程 需要使用manager

class QueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 从网络上获取，注册时只需要名字
    QueManager.register("get_task_que")
    QueManager.register("get_result_que")
    print("Connecting server")
    manager = QueManager(address=("localhost", 18080), authkey=b"abc")

    manager.connect()

    task = manager.get_task_que()
    result = manager.get_result_que()

    while True:
        try:
            n = task.get()
            result.put(n + 1)
            print("put: %s" % str(n + 1))
        except queue.Empty:
            print("result is empty")


    # manager.shutdown()
