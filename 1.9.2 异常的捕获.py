"""
try:
    可能出错的代码
expect:
    如果出错执行的代码
"""

try:
    f = open("test.txt", "r")
except:
    f = open("test.txt", "w")


# 捕获指定异常
try:
    print(name)
except NameError as ne:
    print("出现了变量未定义错误")
    print(ne)

# 捕获多个异常
try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as zde:
    print(zde)

# 捕获所有的异常
try:
    print(1 / 0)
    print(name)
except Exception as e:
    print(e)

# else表示没有异常后执行的语句
# finally表示无视异常与否都去执行
try:
    print(1 / 1)
except Exception as er:
    print(er)
else:
    print("未发现异常")
finally:
    print("hello")

