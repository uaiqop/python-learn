"""
__str__魔术方法
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


stu = Student("Aaron", 15)
# 输出内存地址
print(stu)
print(str(stu))

# 可以通过__str__控制类转换为字符串的行为
class Student1:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def __str__(self):
        return f"姓名：{self.name} 年龄：{self.age}"

stu = Student1("John", 16)
# 不再输出内存地址，而是输出__str__中的内容
print(stu)
print(str(stu))

"""
__lt__小于符号比较方法
"""
class Student2:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def __str__(self):
        return f"姓名：{self.name} 年龄：{self.age}"

    def __lt__(self, other):
        return self.age < other.age

stu = Student2("John", 16)
stu1 = Student2("Mike", 13)
# 对两个对象的age进行比较
print(stu < stu1)
print(stu > stu1)

"""
__le__魔术方法
"""

# 适用于小于等于大于等于的比较
# 类似于lt，如法砲制即可

"""
__eq__魔术方法
"""

# 适用于验证两边是否相等
# 类似于lt，如法砲制即可

