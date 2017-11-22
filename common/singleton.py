# 如何实现一个类的单例

# 方法一, 利用装饰器的闭包原理


def singleton(cls):

    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper

# 这个更为优雅


def singleton_better(cls):

    instance = cls()
    instance.__call__ = lambda: instance
    return instance

print("#################begin test for singleton")


@singleton
class Test(object):

    def __init__(self):
        print("####__INIT--")

t1 = Test()
print(id(t1))
t2 = Test()
print(id(t2))

# 方法二, 利用重写类的__new__方法


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        print("########start __new__, input_param:{},{}".format(args, kwargs))
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance


class Test1(Singleton):

    def __init__(self, a, b):
        print("######## start __init__")
        self.a = a
        self.b = b
        print("######param a:{}, b{}".format(self.a, self.b))


print("#################begin test1 for singleton")
t1 = Test1(a=1, b=2)
t2 = Test1(a=1, b=3)
print(id(t1))
print(id(t2))

# 利用元类实现单例 下述例子需要在py2的环境下运行


class Singleton1(type):

    def __init__(cls, name, bases, attrs):
        print("create metaclass====,{},{},{}".format(name, bases, attrs))
        super(Singleton1, cls).__init__(name, bases, attrs)  # 可用这样的形式创建类型: type(class_.__name__, (class_,), {}),
        cls._instance = None                                 # type 是制造类的类

    def __call__(cls, *args, **kwargs):
        print("created Test2 object===")
        if not cls._instance:
            cls._instance = super(Singleton1, cls).__call__(*args, **kwargs)
        return cls._instance


class Test2(object):

    __metaclass__ = Singleton1

    def __init__(self, a, b):
        print("######## start __init__")
        self.a = a
        self.b = b
        print("######param a:{}, b{}".format(self.a, self.b))


print("#################begin test2 for singleton")
print("##########,{}".format(Test2.__class__), isinstance(Test2, Singleton1))
t1 = Test2(1, 2)
t2 = Test2(2, 3)
print(id(t1))
print(id(t2))
