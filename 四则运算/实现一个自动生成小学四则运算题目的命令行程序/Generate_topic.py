from size_topic import *
from Grade import *
def num_topic(times,r,randomNum,filename1='Exercise.txt',filename2='Answer.txt'):
    """用户输入"""
    operator_num = randomNum
    if operator_num < 1 or operator_num > 3:
        print("请重新输入(1,2,3)")  # 本程序仅支持1~3个符号运算
    elif operator_num == 1:
        one_size_topic(times,r,filename1='Exercise.txt',filename2='Answer.txt')  # 转到单符号运算
    elif operator_num == 2:
        double_size_topic(times,r,filename1='Exercise.txt',filename2='Answer.txt')  # 转到双符号运算
    elif operator_num == 3:
        triple_size_topic(times,r,filename1='Exercise.txt',filename2='Answer.txt')  # 转到三符号运算
num_topic(3333,10,1)
num_topic(3333,10,2)
num_topic(3334,10,3)
Check()



