"""
私有成员：无法直接被类对象所使用，无法直接被类对象赋值或者获取值，但是可以被类中的其他成员所使用
定义方法：变量或函数以两个下划线开头
"""


class test_class:
    __num = 1
    __str = "hello world"

    def __test(self):
        print("you can't use it")

    def test(self):
        print(self.__str)
        self.__test()


my_test = test_class()
my_test.test()
