import threading

local_school = threading.local()  # 全局的thread共享变量


def procees_stu():
    stu = local_school.student
    print("hello " + stu)


def procees_run(name):
    local_school.student = name  # 这里的local_school.student 是一个thread local, 它是每一个线程持有的，各线程对它的访问不会互相干扰
    procees_stu()


t1 = threading.Thread(target=procees_run, args=("Bob",),name="t1")
t2 = threading.Thread(target=procees_run, args=("Alice",),name="t2")
t1.start()
t2.start()
t1.join()
t2.join()
