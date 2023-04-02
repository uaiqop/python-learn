"""
发工资
一共20名员工，绩效1-10分随机生成，从员工1开始依次领取工资
- 绩效低于5，不发工资
- 高于等于5，发1000
- 如果资金用完，结束发工资
"""
import random
money = int(input("输入资金余额："))
for x in range(1, 21):
    point = random.randint(1, 10)
    if money < 1000:
        print(f"资金不足，结束发工资")
        break
    elif point >= 5:
        money -= 1000
        print(f"员工{x}绩效为{point}，大于等于5，发1000元工资，资金还剩{money}")
    else:
        print(f"员工{x}绩效小于5，不发工资")
        continue
