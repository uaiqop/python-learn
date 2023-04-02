for x in range(1, 6):
    print(1)
    # 使用continue跳过本次循环，直接执行下一次循环，也可以用于while循环
    continue
    print(2)

print()

for y in range(1, 5):
    print(5)
    # 使用break跳过这个循环，直接执行下面的“stop”，也可用于while循环
    break
    print("hello")
print("stop")
