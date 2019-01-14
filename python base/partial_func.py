'''偏函数的作用就是将函数的某些参数确定下来'''
import functools

print(int(1))
print(int("1011100", base=2))  # 这样写太复杂

int2 = functools.partial(int, base=2)  # 这里的作用就是将int的base参数确定下来，固定默认值，并返回一个新函数以供调用
print(int2("10001001"))
