age = int(input("请输入年龄："))
if age >= 60:   # 如果
    print("老年")
elif age >= 18:
    print("成年")
elif age >= 14:     # 否则，如果...
    print("青少年")
else:
    print("儿童")
