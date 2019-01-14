'''list generate pattern'''
x1 = [x for x in range(1, 10)]

print(x1)
x1 = [x ** 2 for x in range(1, 10)]
print(x1)

# 生成全排列
print([m + n for m in "AB" for n in "CD"])

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x for x in L1 if isinstance(x, str)]
print(L2)

'''list generator'''
# 生成式
x1 = [x for x in range(1, 10)]
print(type(x1))  # <class 'list'>
# 方式1 生成器,用（）包含
x2 = (x for x in range(1, 10))
print(type(x2))  # <class 'generator'>

# for i in x2:
#     print(i)


# 方式2 ,使用yield 关键字
def gen(start, end):
    for i in range(start, end):
        yield i


g1 = gen(1, 10)
print(g1) #generator object
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
# for i in g1:
#     print(i)

# 为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

