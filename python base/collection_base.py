from collections import namedtuple, deque, defaultdict, OrderedDict

#  a tuple with a special type name which has two properties named x and y
Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)

print(p1.x)
print(isinstance(p1, Point))

# deque. a bidirection linked list which is highly effective in inserting and deleting

q = deque([1, 2, 3])
q.append(4)
print(q)
q.insert(1, 100)
print(q)
print(q.pop())
print(q)
q.appendleft(-1)
print(q)

default_dict = defaultdict(lambda x: "Null")
print(default_dict.get("abc"))

order_dic = OrderedDict()