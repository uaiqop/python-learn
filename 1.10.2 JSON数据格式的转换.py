import json
"""
json是各个编程语言沟通的桥梁
不同的语言的数据容器不同，所以需要json作为中转站
"""

data = [{"name": "Aaron", "age": 16}, {"name": "John", "age": 15}]

# 将python数据转换为json数据
data = json.dumps(data)
print(type(data))
print(data)
# 将json数据转换为python数据
data = json.loads(data)
print(type(data))
print(data)
