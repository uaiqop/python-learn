"""
- 局部变量指的是在函数体内部的变量，只在函数体内部生效，无法在函数外调用
- 全局变量指的是在函数体内，外都能生效的变量
"""


def say_hello():
    # 定义一个局部变量
    hello = "hello world"
    print(hello)


# 定义一个全局变量
a = "hello"


def say():
    hello = "world"    # 与上面那个函数的hello变量不是同一个变量
    print(a + hello)


say_hello()
say()

world = "hello"
print(world)


# 使用global关键字，可以将函数内的变量声明为全局变量
def hello():
    global world    # 声明后，函数内的world变量与函数外的world变量为同一个变量
    world = "hello world"
    return None


hello()
print(world)
