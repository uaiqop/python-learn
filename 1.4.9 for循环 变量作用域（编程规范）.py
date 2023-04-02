"""
for 临时变量
临时变量在编程规范上，作用范围只限定在for循环内部
实际上在for外是可以访问到的
"""

for x in range(5):
    print(x)
print(x)