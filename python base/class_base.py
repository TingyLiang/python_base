class Animal(object):
    def run(self):
        pass


class Dog(Animal):
    # 类属性
    count = 0

    def __init__(self):
        self.blood = "husky"  # public field
        self.__gender = "male"  # private field,实际会被改名为_Dog__gender
        Dog.count += 1

    def run(self):
        print("A dog is running")

    # 这里私有方法会被修改为_Dog__private_run
    def __private_run(self):
        pass


c = Dog.__class__
print(type(c))
print(dir(Dog))  # 获取一个类的属性和方法,如果是类，只能获取类变量，不能获取实例变量

dog = Dog()
dir(dog)
print(Dog.count)
print(dog.blood)
print(dog._Dog__gender)  # 这里访问了dog 的gender字段

'''下面测试动态绑定'''


class Student(object):
    __slots__ = ("_name", "score", "location", "hello")  # 限定只能动态绑定slots中的变量，且，这个限定在子类中不生效

    def __init__(self, name="unknow"):
        self._name = name
        pass

    # 属性访问控制的装饰器, 如果仅定义读方法，不定义set方法，则该属性为只读属性
    @property
    def name(self):
        return self._name

    @name.setter  # 这里的XXX.setter, XXX须是在@property定义的属性名方法名，否则会无法解析,这里的参数不可与属性名同名，否则会引起冲突
    def name(self, new):
        if new:
            self._name = new
        else:
            raise ValueError("attribute name can not be None")

    # 定义此方法，可以把对象当做函数调用
    def __call__(self, *args, **kwargs):
        print("my name is " + self.name)


alice = Student("Alice")
bob = Student("Bob")
bob()  # 调用对象，这里实际是调用__call__方法
# 属性绑定
# stu.name = "Alice"
alice.score = 93
# alice.name = None
alice.name = "Alice"
# alice.name("Alice") #  setter 不能直接调用，而是应该alice.name = "Alice",这样调用会获取到getter方法的函数变量，无法获得正确结果
print("new name:" + alice.name)
print(alice.name)


# bob.abc = "test" 这里不能对未在slots里面定义的变量进行动态绑定，会报错

# 方法绑定

def hello(self):
    print("hello")


def hello_2(self, name):
    print("hello:" + name)


# bind a func to stu 绑定方法到对象，只对当前对象有效
from types import MethodType

alice.hello = MethodType(hello, alice)  # 第二个参数是要绑定的对象
alice.hello
# bob.hello   这里会报错，因为hello方法只绑定到alice

# bind a func to a class，绑定方法到类，所有的对象均可使用

Student.hello_2 = hello_2
ted = Student("ted")
david = Student("david")

ted.hello_2("alice")
david.hello_2("lty")


# 下面测试多重继承
class runnableMixIn(object):
    count_thread = 0

    def __init__(self):
        pass

    def run(self):
        print("run in runnableMixIn")

    def __pri_run(self):
        print("private run in runnableMixIn")

    @staticmethod  # 静态方法
    def __sta_fun__():
        print("static fun  in runnableMixIn")

    @classmethod  # 类方法
    def __increase_thread__(cls):
        cls.count_thread += 1
        print(cls.count_thread)


class AnotherMixIn(object):
    def __init__(self):
        pass

    def foo(self):
        print("foo in AnotherMixIn")


class TestMixIn(runnableMixIn, AnotherMixIn):
    def __init__(self):
        pass


mixIn = TestMixIn()
mixIn.run()  # 这里就可以使用父类的方法
# mixIn.__pri_run() 私有方法不能继承
# 静态类方法，
mixIn.__sta_fun__()
TestMixIn.__sta_fun__()

TestMixIn.__increase_thread__()
