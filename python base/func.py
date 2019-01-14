L1 = [x for x in range(1, 10)]

print(list(map(lambda x: x ** 2, L1)))


# list = [x for x in range(1, 1000)]


def check(n):
    n = str(n)
    i = 0
    l = len(n) - 1
    while i < l / 2:
        if n[i] != n[l - i]:
            return False
        i += 1
    return True


print(check(323))

#  sorted

li = [1, 3, -9, 5, 0, -200]
# 使用函数作用于
print(sorted(li, key=abs))


# 返回函数，return a function,这里也称为函数闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def lazy_sum(*kwargs):
    def sum():
        _sum = 0
        for i in kwargs:
            _sum += i
        return _sum

    return sum


l_sum = lazy_sum(1, 3, 2, 3)  # now l_sum is just a function object
print(l_sum)  # <function lazy_sum.<locals>.sum at 0x00000000028FA730>
print(l_sum())  # actually call the function, now we get 9 here


def createCounter():
    i = 0

    def counter():
        nonlocal i  # 使用这个关键字可以使编译器自动查找外部变量
        i += 1
        return i

    return counter


# def createCounter():
#     f = [0]
#
#     def increase():
#         f[0] = f[0] + 1
#         return f[0]
#
#     return increase


counterA = createCounter()

print(counterA.__name__)  # 获取函数的名字
print(counterA())
print(counterA())
print(counterA())
print(counterA())

l = [x for x in range(1, 20)]
# print(l)
L = list(filter(lambda x: x % 2 == 1, l))

print(L)
