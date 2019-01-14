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


alice = Student("Alice")
bob = Student("Bob")
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
