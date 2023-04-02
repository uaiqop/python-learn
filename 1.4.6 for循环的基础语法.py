# for循环是对一批数据逐个处理
"""
for 临时变量 in 待处理数据集（序列类型）
    执行代码
"""
name = "hello"
for x in name:
    print(x)

num = {1, 9, 50, 37}
for x in num:
    print(x)

i = 0
word = input("输入一个单词：")
for x in word:
    i += 1
print(f"有{i}个字母")