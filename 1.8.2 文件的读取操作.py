"""
open(name, mode, encoding)
name是文件路径
mode是打开方式，有r（只读），w（覆盖内容，从头开始编辑），a（追加，在文件后方继续写入）
"""

# 打开文件
f = open("./test.txt", "r", encoding="UTF-8")
print(type(f))

# 读取文件
print(f.read(4))
# read(num)，num表示要读取的长度，留空则全部读取
print(f.read())
# 上面读取了四个字节，指针移动到了第四个字节后，再执行全部读取就只会读取指针所在处后面的字节

# 以列表的形式返回
print(f.readlines())
# 在这里读取返回不出结果，因为上面把全部文件都读取了，指针已经移动到了最后面

# 只读取一行
print(f.readline())

# 关闭文件
f.close()

# 使用with open使文件操作完成后自动关闭文件
with open("./test.txt", "r", encoding="UTF-8") as f:
    print(f.readlines())

# 在with中打开文件，操作完成后会自动关闭




