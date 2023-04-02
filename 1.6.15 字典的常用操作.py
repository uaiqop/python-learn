# 新增元素：字典[Key] = Value
a = {
    "a": 45,
    "b": 55,
    "c": 90
}
a["d"] = 35
print(a)

# 更新元素
a["d"] = 78
print(a)

# 删除元素：字典.pop(Key)
a.pop("d")
print(a)

# 获取全部key
keys = a.keys()
print(keys)

# 统计元素
print(len(a))


# 清空
a.clear()
print(a)
