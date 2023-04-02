# 定义一个函数统计字符串长度，并且不使用len()
str1 = "hello"
str2 = "world"
str3 = "me"


# 定义一个叫做len1的函数
def len1(data):
    count = 0
    for i in data:
        count += 1
    print(count)


# 调用len1
len1(str1)
len1(str2)
len1(str3)
