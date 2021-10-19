from Generate_topic import *
from Grade import *
import argparse
import os
parser = argparse.ArgumentParser(description="小学四则运算自动生成器")#命令行参数输入
parser.add_argument('-n', '-na', type=str, default=0, help='控制生成题目的个数')
parser.add_argument('-r', '-ra', type=str, default=0, help='题目中数值（自然数、真分数和真分数分母）的范围')
parser.add_argument('-o', '-oa', type=str, default=0,help='控制生成运算符的个数')
parser.add_argument('-e', '-ea', type=str, default="", help='题目文件')
parser.add_argument('-a', '-aa', type=str, default="", help='答案文件')
args = parser.parse_args()
n = int(args.n)
r = int(args.r)
o = int(args.o)
e = args.e
e = e.strip()
a = args.a
a = a.strip()
if os.path.exists(e) and os.path.exists(a):
    print("核对答案后文件将保存到Grade.txt")
    grade = Check(e,a)
else:
    operatorNum = num_topic(n, r, o)  # 将输入的参数传入num_topic()函数
os.system("pause")
