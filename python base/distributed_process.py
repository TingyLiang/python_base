import queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager
from queue import Queue

task_que = Queue()
result_que = Queue()


### 分布式进程 需要使用manager

class QueManager(BaseManager):
    pass


def get_tasks():
    return task_que


def get_results():
    return result_que


if __name__ == '__main__':
    # 注册两个Queue 到网络上，由于manager管理多个队列，需要给每个队列的网络调用接口起一个名字，比如这里的get_task_que。
    # 使用 callable 关联队列对象 ，但是需要注意的是，pickle模块不能序列化lambda函数，此处需要自定义函数
    # freeze_support()
    QueManager.register("get_task_que", callable=get_tasks)
    # QueManager.register("get_task_que", callable=lambda: task_que)
    QueManager.register("get_result_que", callable=get_results)
    # QueManager.register("get_result_que", callable=lambda: result_que)

    manager = QueManager(address=("localhost", 18080), authkey=b"abc")

    manager.start()

    task = manager.get_task_que()
    result = manager.get_result_que()
    print("putting task...")
    for i in range(10):
        task.put(i)
        print("put: %s" % i)

    print("getting result...")
    for i in range(10):
        try:
            print("result is %s" % result.get(timeout=10))
        except queue.Empty:
            print("result is empty")


    manager.shutdown()
