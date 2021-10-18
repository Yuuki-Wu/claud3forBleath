from size_topic import *


def num_topic(randomNum,r,times):
    """用户输入"""
    topic = []
    result = []
    operator_num = randomNum
    if operator_num < 1 or operator_num > 3:
        print("请重新输入(1,2,3)")  # 本程序仅支持1~3个符号运算
    elif operator_num == 1:
        one_size_topic(r, times)  # 转到单符号运算
    elif operator_num == 2:
        double_size_topic(r, times)  # 转到双符号运算
    elif operator_num == 3:
        triple_size_topic(r, times)  # 转到三符号运算




