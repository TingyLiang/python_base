import functools


def log(fun):
    @functools.wraps(fun)  # *****这里用于重置函数__name__等属性，避免因签名导致的错误
    def wrapper(*args, **kwargs):
        print("called %s" % fun.__name__)
        a = fun(*args, **kwargs)
        print("end call")
        return a

    return wrapper


# 装饰器，用作函数增强，在函数调用前会调用装饰器的内容，相当于log(now)
@log
def now():
    import time
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


now()
a = now
print(now.__name__)  # 没有使用functools.wrap()前的函数名 wrapper
print(now.__qualname__)
print(now.__annotations__)
print(now.__call__)
