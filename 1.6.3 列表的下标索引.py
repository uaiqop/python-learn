# 列表有顺序，从0开始，每个元素对应的数字就是下标索引
name = ["Aaron", "John", "Mike"]
print(name[0])
print(name[2])
print(name[1])
print(type(name[1]))

# 可以反向索引，从后向前，从-1开始，依次递减
print(name[-1])
print(name[-3])
print(name[-2])
print()
# 嵌套列表同样支持下标索引
b = [[1, 2], ["hello", "world"]]
print(b[1][0])
print(b[0][0])

print()

c = [[1, 2], [["hello", "world"], True]]
print(c[1][-2][1])
