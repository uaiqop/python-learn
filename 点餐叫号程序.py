import locale

customer = []
name = ""
text = "请[customer]到前台取餐"
lang = []
language = ""


def language_choose():
    global language
    while True:
        choose1 = input("""
1.简体中文（中国）  \t我能吞下玻璃而不伤身体
2.繁體中文（臺灣）  \t我能吞下玻璃而不傷身體
3.繁體中文（香港）  \t我能吞下玻璃而不傷身體
4.English(UK)   \tI can eat glass, it doesn't hurt me.
5.English(US)   \tI can eat glass, it doesn't hurt me.
""")
        if choose1 == "1":
            language = "zh_cn"
            return "zh_cn"
        elif choose1 == "2" or "3":
            language = "zh_tw"
            return "zh_tw"
        elif choose1 == "4" or "5":
            language = "en_us"
            return "en_us"
        else:
            print("against")


def lang_reply():
    global lang
    lang = []
    zh_cn = ["""
    主页/增加顾客
    请输入顾客名称(输入exit返回)：""", "请输入名称", f"""
    *****************************************
    增加成功，{name}排在第{len(customer)}位
    *****************************************
    """, """
    **************
    列表中没有顾客了
    **************
    """, f"""
    主页/设置/修改叫号文本
    更换叫号的文本内容
    顾客名称使用[customer]代替
    例如：请[customer]到前台取餐
    当前的文本内容：{text}
    请输入新的文本内容（输入exit返回）：""", "文本中找不到[customer]，无法叫号，请重新输入", """
    **********
    增加成功
    **********""", """
    主页/设置
    1.修改叫号文本
    2.更新日志
    3.关于
    4.返回
    请输入数字：""", "请输入正确数字", """
    主页
    1.增加顾客
    2.下一位顾客
    3.设置
    4.退出
    请输入数字：""", "请输入正确数字", "欢迎使用叫号程序"]
    zh_tw = ["""
主頁/新增顧客
請輸入顧客名稱（輸入exit返回）:""", "請輸入名稱", f"""
*****************************************
新增成功,{name}排在第{len(customer)}比特
*****************************************
""", """
**************
清單中沒有顧客了
**************
""", f"""
主頁/設定/修改叫號文字
更換叫號的文字內容
顧客名稱使用[customer]代替
例如：請[customer]到前臺取餐
當前的文字內容：{text}
請輸入新的文字內容（輸入exit返回）：""", "文字中找不到[customer],無法叫號,請重新輸入", """
**********
新增成功
**********""", """
主頁/設定
1.修改叫號文字
2.更新日誌
3.關於
4.返回
請輸入數位：""", "請輸入正確數位", """
主頁
1.新增顧客
2.下一位顧客
3.設定
4.退出
請輸入數位：""", "請輸入正確數位", "歡迎使用叫號程式"]
    en_us = ["""
    Home/Add Customer
Please enter the customer name (enter exit to return):""", "Please enter a name", f"""
    *****************************************
    Successfully added, {name} ranked {len(customer)}
    *****************************************
    """, """
    **************
    There are no more customers in the list
    **************
    """, f"""
    Home/Settings/Modify Call Text
Change the text content of the call
Use [customer] instead of the customer name
For example, please ask [customer] to pick up the meal at the front desk
Current text content: {text}
Please enter a new text content (enter exit to return):""",
             "Unable to find [customer] in the text, unable to call, please re-enter", """
    **********
    Successfully added
    **********""", """
    Home/Settings
1. Modify the call text
2. Update Log
3. About
4. Return
Please enter a number:""", "Please enter the correct number", """
    homepage
1. Add customers
2. Next customer
3. Settings
4. Exit
Please enter a number:""", "Please enter the correct number", "Welcome to the station calling program"]
    global language
    locale.getlocale()
    sys_lang = locale.getdefaultlocale()
    if language == "zh_cn":
        lang = zh_cn
    elif language == "zh_tw":
        lang = zh_tw
    elif language == "en_us":
        lang = en_us
    else:
        if sys_lang[0] == "zh_CN":
            lang = zh_cn
            language = "zh_cn"
        elif sys_lang[0] == "zh_TW":
            language = "zh_tw"
            lang = zh_tw
        elif sys_lang[0] == "zh_HK":
            language = "zh_tw"
            lang = zh_tw
        elif sys_lang[0] == "en_US":
            language = "en_us"
            lang = en_us
        elif sys_lang[0] == "en_GB":
            language = "en_us"
            lang = en_us
        else:
            choose1 = language_choose()
            if choose1 == "zh_cn":
                lang = zh_cn
            elif choose1 == "zh_tw":
                lang = zh_tw
            elif choose1 == "en_us":
                lang = en_us
            else:
                print("error")


def add():
    """
    增加顾客
    :return:
    """
    while True:
        global name
        name = input(lang[0])
        if name == "":
            print(lang[1])
            continue
        elif name == "exit":
            break
        else:
            customer.append(name)
            lang_reply()
            print(lang[2])
            break


def next_customer():
    """
    叫号
    :return5
    """
    if not customer:
        print(lang[3])
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

1.1.0.230317_alpha
增加了繁体中文、英文翻译

1.1.1.230318_beta
修复了已知bug

1.1.1.230318_release
修复已知bug
更改关于页面的程序名称
""")


def text_edit():
    """
    叫号文本修改
    :return:
    """
    # 声明 text 为全局变量
    global text
    while True:
        new_text = input(lang[4])
        lang_reply()
        if new_text == "exit":
            break
        elif new_text.find("[customer]") == -1:
            print(lang[5])
            continue
        else:
            text = new_text
            print(lang[6])
            break


def setting():
    """
    设置页面
    :return:
    """
    while True:
        choose1 = input(lang[7])
        if choose1 == "1":
            text_edit()
        elif choose1 == "2":
            update_log()
        elif choose1 == "3":
            about()
        elif choose1 == "4":
            break
        else:
            print(lang[8])


def about():
    """
    关于页面
    :return:
    """
    print("*********************************************")
    print("通用叫号程序")
    print("1.1.1")
    print("10940 吴彦炜")
    print("一个通用的叫号工具，在餐厅、银行等地方都可以使用")
    print("""本程序不作任何担保。
详情请见 GNU 通用公共许可证，第 3 版及以上(https://www.gnu.org/licenses/gpl-3.0.html)。""")
    print("*********************************************")


# main
lang_reply()
print(lang[11])
while True:
    choose = input(lang[9])
    if choose == "1":
        add()
    elif choose == "2":
        next_customer()
    elif choose == "3":
        setting()
    elif choose == "4":
        break
    else:
        print(lang[10])
