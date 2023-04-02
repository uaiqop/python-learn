print("你的名字是？")
name = input()  # 获取键盘输入信息
print("你的名字是%s" % name)

# input可以直接输出提示
age = input("你的年龄是？")
print("你%s岁了" % age)

# input语句读取的信息类型都是字符串
num = input("输入一个数字")
print("类型：%s" % type(num))
