# 如何实现一个类的单例

# 方法一, 利用装饰器的闭包原理, 装饰器的作用导致在文件加载的时候,把类当作对象传入,
# 而实际返回的类名已经变成了一个判定是否生实例化类的函数


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
print(Test, type(Test))
t1 = Test()
print(id(t1))
t2 = Test()
print(id(t2))

# 方法二, 利用重写类的__new__方法
# object是所有类的基类
# 注意:该方式会因为每次都进入了基类的__new__方法,虽然没有创建新的实例对象,但是会默认__new__方法执行完毕,把参数传入__init__方法
# 所以能够使得每次__init__初始化的值都不一样,如果你运用单例模式不希望初始值被改变,则需要慎用。


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
# 元类是创建类的类, 当指定一个类的元类的时候, 在文件加载的时候会调用元类的__init__方法来创建这个类
# 而当我们用cls()来创建实例的时候,其实等同于metaclass(name, bases, attrs)(), 调用元类的__call__方法,
# 所以我们可以利用这个原理来执行cls的__init__之前来做点什么, __call__执行的过程中会执行cls的__new__,其次cls的__init__,借此来实现单例模式


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
