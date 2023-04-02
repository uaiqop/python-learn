def a(one, two, three):
    print(one, two, three)
    return "ok"


# 位置参数（必须按顺序）
a("这是one", "这是two", "这是three")
# 关键词传参（不用按顺序）
a(three="这是3", one="这是1", two="这是2")
# 混合
a("这是1", three="这是3", two="这是2")


# 缺省参数：也叫默认参数，当没有传递参数时，使用默认值
def b(age, gender, hello="你好"):
    print(age)
    print(hello)
    return


b(14, "男", )


# 位置不定长（不确定调用的时候会传递多少个参数）
def c(*num):
    print(num)
    return 0


c(1, 4, 5, 8)


# 关键词不定长
def d(**dic):
    print(dic)
    return 0


# 类似于字典
d(o="114514", p="1919810")
