"""
元组使用小括号定义
元组一旦被定义就不可以修改
"""

# 定义元组
t = (1, "hello", True)
print(t)
t2 = tuple()
print(t2)

# 如果元组内只写一个元素，那么后面要加逗号
t3 = (2333, )
print(t3)

# 嵌套
t4 = ((1, 3, 5),  ("a", "b", "c"))
print(t4[0][0])

# 下标索引取出内容
print(t4[1][0])

# index查找
t5 = (1, 8, 10, 8)
i = t5.index(8)
print(i)

# count统计
i = t5.count(8)
print(i)

# len 统计
i = len(t5)
print(i)
