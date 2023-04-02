import random
i = True
num = random.randint(1, 100)
while i:
    guess_num = int(input("输入1到100之间的数字："))
    if guess_num > num:
        print("小一点")
    elif guess_num < num:
        print("大一点")
    else:
        print("猜对了")
        i = False
