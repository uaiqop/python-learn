f = open("./test.txt", "w")

# 文件写入
f.write("""hello world
你好世界
使用write写入
""")
# 执行write时内容并未真正写入文件，而是会积攒在程序的内存里，称之为缓冲区

# 使用flush让缓冲区的内容写入文件
f.flush()

# 关闭文件
f.close()
# close内置flush的功能，在关闭文件同时写入


"""
文件的追加操作与写入基本相同，如法泡制即可
"""