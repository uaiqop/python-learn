customer = []
text = "请[customer]到前台取餐"


def add():
    """
    增加顾客
    :return:
    """
    while True:
        name = input("""
主页/增加顾客
请输入顾客名称(输入exit返回)：""")
        if name == "":
            print("请输入名称")
            continue
        elif name == "exit":
            break
        else:
            customer.append(name)
            print(f"""
*****************************************
增加成功，{name}排在第{len(customer)}位
*****************************************
""")
            break


def next_customer():
    """
    叫号
    :return5
    """
    if not customer:
        print("""
**************
列表中没有顾客了
**************
""")
    else:
        print("\n*****************************\n", text.replace("[customer]", f"{customer[0]}"),
              "\n*****************************")
        del customer[0]


def update_log():
    """
    更新日志
    :return:
    """
    print("""
1.0.0.221225_alpha
实现了简单的叫号功能，但是只能按照自动编排的号数叫号

1.0.0.230106_alpha
实现了自定义号数

1.0.0.230108_beta
优化了代码，将功能模块化，方便调试

1.0.0.230130_RC
实现了自定义客户名称

1.0.0.230219_release
更新版本号

1.0.0.230219_release1
增加更新日志选项

1.0.1.230223_release
增加了修改叫号文本功能，泛用性更强
优化了代码，修复了部分bug

1.0.1.230223_release1
增加了设置页面，将部分选项整合进设置
在每个页面上方显示了目录层级，并且在大多数页面增加了返回功能

1.0.1.230314_release1
规范了输出格式
更改了关于页面
""")


def text_edit():
    """
    叫号文本修改
    :return:
    """
    # 声明 text 为全局变量
    global text
    while True:
        new_text = input(f"""
主页/设置/修改叫号文本
更换叫号的文本内容
顾客名称使用[customer]代替
例如：请[customer]到前台取餐
当前的文本内容：{text}
请输入新的文本内容（输入exit返回）：""")
        if new_text == "exit":
            break
        elif new_text.find("[customer]") == -1:
            print("文本中找不到[customer]，无法叫号，请重新输入")
            continue
        else:
            text = new_text
            print("""
**********
增加成功
**********""")
            break


def setting():
    """
    设置页面
    :return:
    """
    while True:
        choose1 = input("""
主页/设置
1.修改叫号文本
2.更新日志
3.关于
4.返回
请输入数字：""")
        if choose1 == "1":
            text_edit()
        elif choose1 == "2":
            update_log()
        elif choose1 == "3":
            about()
        elif choose1 == "4":
            break
        else:
            print("请输入正确数字")


def about():
    """
    关于页面
    :return:
    """
    print("****************************************************************************************************")
    print("多用叫号程序")
    print("1.0.1")
    print("10940 吴彦炜")
    print("一个多功能的叫号工具，在餐厅、银行等地方都可以使用")
    print("本程序不作任何担保。详情请见 GNU 通用公共许可证，第 3 版及以上(https://www.gnu.org/licenses/gpl-3.0.html)。")
    print("****************************************************************************************************")


# main
print("欢迎使用叫号程序")
while True:
    choose = input("""
主页
1.增加顾客
2.下一位顾客
3.设置
4.退出
请输入数字：""")
    if choose == "1":
        add()
    elif choose == "2":
        next_customer()
    elif choose == "3":
        setting()
    elif choose == "4":
        break
    else:
        print("请输入正确数字")
