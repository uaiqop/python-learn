"""
range可以帮助生成数字序列
"""
i = range(5)    # 从0到5结束的数字序列，不包括5本身
i = range(3, 8)     # 从3开始到8结束，不包括8
i = range(7, 12, 2)     # 从7开始到11结束，数字序列中每俩个序列间隔为2，如7，9，11

for x in range(10):
    print(x)
print("------")
for x in range(3, 10):
    print(x)
print("------")
for x in range(3, 10, 2):
    print(x)
print("------")
for x in range(10):
    print("hello")