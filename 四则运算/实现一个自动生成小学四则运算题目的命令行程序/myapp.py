from Generate_topic import *
from Grade import *
import argparse
import os
g = 'Grade.txt'
randomNum = 0
parser = argparse.ArgumentParser(description="小学四则运算自动生成器")
parser.add_argument('-n', '-na', type=str, help='控制生成题目的个数')
parser.add_argument('-r', '-ra', type=str, help='题目中数值（自然数、真分数和真分数分母）的范围')
parser.add_argument('-e', '-ea', type=str, default=" ", help='题目文件')
parser.add_argument('-a', '-aa', type=str, default=" ", help='答案文件')
args = parser.parse_args()
n = int(args.n)
r = int(args.r)
e = args.e
e = e.strip()
a = args.a
a = a.strip()
randomNum = random.randint(1,3)
operatorNum = num_topic(randomNum,r,n)
if os.path.exists(e) and os.path.exists(a):
    print("核对答案后文件将保存到Grade.txt")
    grade = Check(e,a,g)
os.system("pause")
