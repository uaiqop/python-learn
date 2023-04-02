# 如果将函数定义为class（类）的成员，那么函数会被叫做方法


# 这是一个函数
def say():
    print("hello")


# 这是一个类
class Hello:

    # class中的函数叫做方法
    def say1(self):
        print("world")
        return None


# 方法的使用
# 先获得方法所在的类的对象
hello = Hello()
hello.say1()
