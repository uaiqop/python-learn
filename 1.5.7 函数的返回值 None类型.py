"""
如果一个函数没有使用return语句返回数据，那么就会返回None
"""


# 定义函数
def say_hello():
    print("hello")


# 输出返回值
print(say_hello())
# 输出返回值类型
print(type(say_hello()))


# 也可以手动返回None
def say_none():
    return None


print(say_none())

"""
- 在if判断中，None等同于False
- 定义变量时，暂时不需要有具体值，也可以使用None代替
"""
a = None
print(type(a))