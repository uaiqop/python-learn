"""
集合的特点：不重复（自带去重），内容无序
"""

# 集合定义
a = {1, 8, 9, 6, 4}
print(a)

# 增加新元素
a.add("hello")
a.add(8)
# 自动去重
print(a)

# 移除元素
a.remove(9)
print(a)

# 随机取出元素（集合不支持下表索引）
print(a.pop())

# 清空元素
a.clear()
print(a)
# 清空后结果为set()

# 取两个集合中的差集（集合1有的集合2没有的）
a = {1, 2, 3, 4}
b = {1, 2, 4}
c = a.difference(b)
# 集合a有而集合b没有的
print(c)

# 消除两个集合的差集
a.difference_update(b)
# 在a内删除和b相同的元素
print(a)

# 合并集合
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9}
c = a.union(b)
print(c)

# 统计元素数量
print(len(c))
