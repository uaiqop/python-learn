"""
__init__()方法：在创建类对象时，会自动执行
构建对象是，传入的参数自动传递给__init__()
"""


class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


# 直接传入参数，会将参数传递给__init__()
stu = Student("Aaron", 15)
stu.print_name()
stu.print_age()
