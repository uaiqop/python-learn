ch = ""
while True:
    n = input("请输入排队人数")
    for x in range(1,int(n)+1):
        print("请",str(x),"号到前台取餐")
        ch=input("y：继续叫号，n：退出")
        if ch == "n":
            break
        else:
            print("继续")
    if ch == "n":
        break