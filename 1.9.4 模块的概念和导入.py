# 导入整个时间模块
import time

# print("start")
# time.sleep(1)
# print("stop")


# # 导入时间模块中的sleep函数
# from time import sleep
# print("start")
# # 导入模块中的函数后不需要加time前缀
# sleep(1)
# print("stop")

# # 使用*导入所有函数
# from time import *
# print("start")
# clock(1)
# print("stop")

# 导入模块中的一个函数并定义一个别名
from time import clock as cl
print("start")
cl(1)
print("stop")
