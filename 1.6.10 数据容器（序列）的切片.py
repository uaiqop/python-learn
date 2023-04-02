"""
列表，元组，字符串都可以视为序列
序列的切片指的是从一个序列中取出一个子序列（序列的一部分）
语法：序列[起始下标:结束下标：步长]
步长表示隔几个元素取一次，步长1就是一个个取元素，步长2表示每次跳过一个元素取
步数为负表示反向取
"""

# 对alist进行切片
alist = [1, 2, 3, 4, 5, 6]
blist = alist[1:4:2]
print(blist)

# 从头到尾进行切片，步数为2
blist = alist[::2]
print(blist)

# 倒着切
blist = alist[4:1:-2]
print(blist)

