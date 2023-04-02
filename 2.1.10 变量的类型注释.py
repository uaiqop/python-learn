"""
注释这个变量的类型
语法：
变量: 类型
"""
import random
var_1: int = 222
var_2: float = 3.1415
var_3: str = "hello"
var_4: bool = True

# 类对象的类型注释
class Student:
    pass
stu: Student = Student()

# 容器的注释
my_list: list[int] = [1, 4, 6]
my_tuple: tuple[str, int, float] = ("hello", 23, 2.3940)
my_dict: dict[str, int] = {"hello": 555}

# 在注释中进行类型注释
var_1 = random.randint(1, 10)   # type: int

# 仅作注释，并不会对类型进行验证和判断
