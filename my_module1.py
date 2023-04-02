# __all__变量：使用 * 导入这个模块时，只能使用这个列表中的元素
__all__ = ["test"]


# 用form my_module1 import *导入模块后，只能使用test函数

def test(a, b):
    print(a + b)


def test1(a, b):
    print(a - b)


if __name__ == '__main__':
    # 只在这个模块运行时调用，其他py导入了这个模块不会调用以下内容
    test(1, 6)
