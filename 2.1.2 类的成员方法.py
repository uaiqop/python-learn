"""
class 类:
    类的属性：即定义在类中的变量（成员变量）
    类的方法：即定义在类中的函数（成员方法）
创建类对象：对象 = 类名称()
"""


# 定义一个类
class Student:
    # 定义成员变量
    name = None
    age = None

    # 定义成员方法
    def print_name(self):
        # self相当于对象的名称，表示类对象自身
        print(self.name)

stu = Student()
stu.name = "Aaron"
stu.age = 15

stu.print_name()