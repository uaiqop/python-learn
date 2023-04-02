"""
定义函数
"""
money = 0


def search_money():
    print(f"当前余额为{money}")
    return money


def add_money(num):
    global money
    money += num
    return money


def get_money(num):
    global money
    money -= num
    return money


def main():
    print("""
欢迎使用ATM
查询余额 \t1
存款 \t2
取款 \t3
退出 \t4""")
    return int(input("请选择："))


"""
无限循环，保证程序不退出
"""
while True:
    choose = main()
    if choose == 1:
        search_money()
    elif choose == 2:
        add_money(int(input("请输入存款金额：")))
        print(f"成功，您的余额为{money}")
    elif choose == 3:
        x = 0
        x = int(input("请输入取款金额："))
        while x > money:
            print("余额不足")
            x = int(input("请再次输入金额："))
        get_money(x)
        print(f"取款成功，您当前余额为{money}")
    elif choose == 4:
        break
    else:
        print("请输入正确数字")
