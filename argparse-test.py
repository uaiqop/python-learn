"""
https://docs.python.org/zh-cn/3.10/library/argparse.html
"""
import argparse

parser = argparse.ArgumentParser(description="一个测试程序")
parser.add_argument("num", nargs="+", type=float, help="这是一个位置参数")
parser.add_argument("-s", "--sum", nargs="+", type=float, help="这是一个可选参数")

args = parser.parse_args()
print(args)
print(args.sum)
print(args.num)
