# 设计一个类（相当于设计一张登记表）
class Student:
    name = None
    gender = None
    age = None

# 创建一个对象（相当于打印一张登记表）
stu_1 = Student()

# 赋值（相当于填写表格）
stu_1.name = "Aaron"
stu_1.gender = "男"
stu_1.age = 16

print(stu_1.name)
print(stu_1.age)
