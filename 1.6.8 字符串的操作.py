# 字符串也有下标
i = "hello world"
print(i[1])

# index，查找特定字符串的下标索引值
print(i.index("o"))

# 替换字符串
i = i.replace("o", "e")
# 将字符串中所有的o换成e
print(i)

# 字符串的分割
i = "hello world python"
i = i.split(" ")
print(i)

# 字符串的规整操作（）去前后空格
i = "    hello world   "
print(i.strip())

i = "114514hello world411541"
print(i.strip("1454"))

# 统计字符串长度
i = "hello"
print(len(i))