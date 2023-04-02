"""
将 用户.txt 中的vip用户进行备份
"""

# 打开原先的用户文件
fr = open("./用户.txt", "r")

# 以写入的方式新建一个 用户.txt.bak 的备份文件
fw = open("./用户.txt.bak", "w")

# for循环读取文件
for line in fr:
    line = line.strip()
    # strip可以去掉每一行的\n，也就是换行符
    if line.split(",")[1] == "normal":
        continue
        # 如果为普通用户，直接跳过循环

    # 否则就将内容写入备份文件中
    fw.write(line)
    # 由于前面去除了换行符，现在要自己加一个换行符
    fw.write("\n")

fr.close()
fw.close()
# 写入文件并且关闭
