# coding:utf-8
# python实现单例模式

# 方法一 使用模块
class Singleton(object):
    def foo(self):
        pass

singleton = Singleton()
# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
# from a import singleton

# 方法二 使用装饰器
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    return _singleton

@Singleton
class A(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(2)
# print(a1 == a2)   # True

# 方法三 使用类
# 注意:用类的instance方法,这样有一个弊端就是在使用类创建的时候,并不是单例了.也就是说在创建类的时候一定要用类里面规定的方法创建
# 单线程中相对安全，多线程中不安全

class Singleton(object):
    def __init__(self):
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # 利用反射,看看这个类有没有_instance属性
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

s1 = Singleton()                # 使用这种方式创建实例的时候,并不能保证单例
s2 = Singleton.get_instance()   # 只有使用这种方式创建的时候才可以实现单例

# 加锁后的版本
import time
import threading

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton

def task(arg):
    obj = Singleton.get_instance(arg)
    print(obj)

for i in range(10):
    t = threading.Thread(target=task, args=[i,])
    t.start()

obj = Singleton.get_instance()
#print(obj)


# 方法四 使用__new__方法实现单例模式
"""
1> 一个对象的实例化过程是先执行类的__new__方法,如果我们没有写,默认会调用object的__new__方法,返回一个实例化对象,然后再调用__init__方法,对这个对象进行初始化,我们可以根据这个实现单例.
2> 在一个类的__new__方法中先判断是不是存在实例,如果存在实例,就直接返回,如果不存在实例就创建.
"""
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(cls, "_instance"):
                    Singleton._instance = super().__new__(cls)
            return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()