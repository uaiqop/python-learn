"""
将容器内依次取出元素进行操作，叫做遍历或者迭代
"""


def list_while():
    """
    使用while循环遍历列表
    :return:
    """
    my_list = ["1111", "hello", "world"]
    # 定义变量用来标记列表的下标
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1


def list_for():
    """
    用for来循环遍历列表
    :return:
    """
    my_list = [1, 2, 3, 4, 5, 6]
    for x in my_list:
        print(x)


# 调用函数
list_while()
list_for()
