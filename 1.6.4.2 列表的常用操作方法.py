a = ["hello", 1, True, [3, 8]]

# 查询某元素的下标
print(a.index("hello"))
# index就是列表对象内置的方法
print()


# 列表的修改
a[0] = "world"  # 修改下标为0的元素为world，就是把hello改成world
print(a)
# 再改回来
a[-4] = "hello"
print(a)
print()


# 插入元素
# 格式：列表.insert(下标,元素)
a.insert(1, "world")
print(a)
print()


# 追加元素
# 将指定元素追加到列表尾部
a.append(114514)
print(a)
# 可以将其他容器的内容取出，追加到列表尾部
a.extend([1919, 810])
print(a)
print()


# 元素的删除
# 语法1
del a[-1]
print(a)
# 语法2
b = a.pop(-1)
print(a)
print(f"被删除的元素是：{b}")
print()


# 删除某元素再列表中的第一个匹配项
# 先增加一个元素
a.append("hello")
# 然后删除第一个hello
a.remove("hello")
print(a)
print()


# 清空列表内容
a.clear()
print(a)
print()


# 统计某元素在列表中的数量
a = [1, 1, 4, 5, 1, 4]
print(a.count(1))
print()


# 统计列表中一共有多少个元素
print(len(a))
